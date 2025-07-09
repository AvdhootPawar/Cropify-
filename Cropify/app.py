# Importing essential libraries and modules

from flask import Flask, render_template, request
from markupsafe import Markup
import numpy as np
import pandas as pd
from utils.fertilizer import fertilizer_dic
import requests
import config
import pickle

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading crop recommendation model

crop_recommendation_model_path = r'D:\TY\SEM V\EDI\EDAI\EDAI\models\RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


# ===============================================================================================

# ------------------------------------ FLASK APP -------------------------------------------------

app = Flask(__name__)

# render home page
@app.route('/')
def home():
    title = 'Cropify - Home'
    return render_template('index.html', title=title)

# render crop recommendation form page
@app.route('/crop-recommend')
def crop_recommend():
    title = 'Cropify - Crop Recommendation'
    return render_template('crop.html', title=title)

# render fertilizer recommendation form page
@app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Cropify - Fertilizer Suggestion'
    return render_template('fertilizer.html', title=title)

# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page
@app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Cropify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        city = request.form.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)

        else:
            return render_template('try_again.html', title=title)

@app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'Cropify - Fertilizer Suggestion'

    crop_name = str(request.form['cropname']).strip()  # Trim whitespace
    try:
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
    except ValueError:
        return render_template('try_again.html', title=title)

    df = pd.read_csv('D:\TY\SEM V\EDI\EDAI\EDAI\datasets\Fertilizer.csv')
    df['Crop'] = df['Crop'].str.strip()  # Trim whitespace in the CSV

    print("Crop Name from Form:", crop_name)  # Debugging
    print("Available Crops in CSV:", df['Crop'].unique())  # Debugging

    crop_data = df[df['Crop'].str.lower() == crop_name.lower()]  # Case-insensitive match

    # Check if crop_data is empty
    if crop_data.empty:
        print("No data found for crop:", crop_name)  # Debugging
        return render_template('try_again.html', title=title)

    # Proceed with calculations if crop data is found
    try:
        nr = crop_data['N'].iloc[0]
        pr = crop_data['P'].iloc[0]
        kr = crop_data['K'].iloc[0]
    except IndexError:
        print("Error accessing crop data for:", crop_name)  # Debugging
        return render_template('try_again.html', title=title)

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]

    if max_value == "N":
        key = 'NHigh' if n < 0 else "Nlow"
    elif max_value == "P":
        key = 'PHigh' if p < 0 else "Plow"
    else:
        key = 'KHigh' if k < 0 else "Klow"

    response = Markup(str(fertilizer_dic[key]))

    return render_template('fertilizer-result.html', recommendation=response, title=title)



# ===============================================================================================

if __name__ == '__main__':
    app.run(debug=True)


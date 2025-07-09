# 🌿 Cropify: Benchmarking Crop Production Innovations and Trends

---

Cropify is a powerful, dual-mode agricultural recommendation system designed to provide intelligent guidance for **crop selection** and **nutrient management**. This project was **proudly sponsored by HYGREENS**, and developed in collaboration with them to seamlessly support both **conventional soil-based farming** and **modern hydroponic environments**, empowering farmers and researchers with data-driven insights.

---

## ✨ Core Functionalities

### 1. Crop Recommendation

Get precise suggestions for the most suitable crops based on real-time environmental and soil conditions:

* **Intelligent Prediction:** Uses a **machine learning model** (Random Forest, trained on a curated Kaggle dataset) to recommend crops.
* **Dynamic Inputs:** Considers **NPK values, pH, rainfall**, and integrates **live temperature & humidity data** fetched via the OpenWeather API.
* **Versatile Use:** Provides recommendations for both traditional and hydroponic setups.

### 2. Fertilizer Recommendation (Hydroponic)

Optimize nutrient levels specifically for your hydroponic systems:

* **Nutrient Gap Analysis:** Calculates the deviation between current and ideal NPK values for selected hydroponic crops.
* **Actionable Suggestions:** Delivers specific, **rule-based corrective nutrient suggestions** to fine-tune your solution.
* **Expert Data:** Leverages real-world optimal NPK data directly from **HYGREENS** to ensure accuracy.
* **Hydroponics-Tailored:** Recommendations are crafted exclusively for water-based, soil-less cultivation.

---

## 🔑 Key Features

* **Data-Driven ML Models:**
    * Robustly trained and evaluated across multiple classifiers, with **Random Forest** chosen for its high accuracy (**99.09%**).
    * Comparative analysis included Naive Bayes, SVM, Decision Tree, and Logistic Regression.
* **Real-Time Weather Integration:**
    * Fetches live temperature and humidity based on city input.
    * Enhances prediction relevance by incorporating current environmental conditions.
* **Hydroponic Hardware Demonstration:**
    * A working prototype using the **Nutrient Film Technique (NFT)** regulates nutrient flow.
    * Simulates real hydroponic setups, providing practical proof of concept for the software's recommendations.

---

## 📸 Screenshots

Here are a few glimpses of Cropify in action, showcasing its user interface and functionalities. To add your own screenshots, replace the `alt text` and `path/to/your/image.png` with your actual details.

### Main Dashboard / Input Form

![Screenshot of the Main Dashboard or Input Form](assets/screenshots/dashboard-or-input.png)
*Example: A clear shot of the primary interface where users input data.*

### Crop Recommendation Result Page

![Screenshot of Crop Recommendation Result Page](assets/screenshots/crop-result-page.png)
*Example: Showing the predicted crop and reasoning for the recommendation.*

### Hydroponic Fertilizer Recommendation Output

![Screenshot of Hydroponic Fertilizer Recommendation Output](assets/screenshots/fertilizer-output.png)
*Example: Displaying the calculated nutrient adjustments and suggestions.*

### Hardware Prototype in Action

![Screenshot of the Hardware Prototype](assets/screenshots/hardware-demo-in-action.jpg)
*Example: A photo of your physical NFT setup or other hardware demonstration.*

---

## 🛠️ Technical Stack

### Backend

* Built with **Flask (Python)** for robust web application handling.
* Integrates ML models via `.pkl` files for efficient predictions.
* Utilizes the **OpenWeather API** for real-time data.
* Implements a dedicated **rule-based engine** for fertilizer logic.

### Frontend

* Developed using **Jinja2-based HTML templates**.
* Features clean, user-friendly input forms.
* Provides dynamic rendering of results for both crop and fertilizer suggestions.

### Architecture Highlights

* **Object-oriented model** handling for clean code.
* **CSV-based fertilizer dataset** with integrated preprocessing.
* **Proportional nutrient gap analysis** for precise hydroponic recommendations.
* Robust **exception handling** and clear user feedback mechanisms.

---

## 🌱 Vision & Impact

Cropify aims to bridge the gap between traditional agriculture and modern hydroponic techniques. It's designed as a scalable, smart, and data-driven decision support tool for **sustainable farming**. By seamlessly integrating machine learning, real-time weather data, and expert domain knowledge, Cropify empowers farmers to **boost yield, conserve resources, and make more informed agronomic decisions**.

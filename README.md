# 🚗 Car Price Prediction  
⭐ End-to-End Machine Learning Project

A Machine Learning web application that predicts the resale value of used cars using **Multiple Linear Regression**.  
Built to develop strong fundamentals in data preprocessing, feature engineering, model training, and real-world deployment.

---

## 📌 Overview

Used car pricing depends on multiple variables such as brand, fuel type, vehicle age, and kilometers driven.  
This project trains a regression model on historical data and deploys it with **Streamlit** to deliver instant price predictions through an interactive interface.

---

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy, Scikit-learn**
- **Matplotlib, Seaborn**
- **Streamlit**
- **Git & GitHub**

---

## 🔥 Key Features

✅ Cleaned and preprocessed real-world dataset  
✅ Feature engineering with **Car Age** calculation  
✅ One-Hot Encoding for categorical variables  
✅ Multiple Linear Regression model  
✅ Interactive Streamlit UI  
✅ Real-time price prediction  

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Preparation
- Removed inconsistencies  
- Converted price and kms-driven columns to numeric  

### 2️⃣ Feature Engineering
- Derived `car_age` from manufacturing year  
- Encoded categorical variables  

### 3️⃣ Model Training
- Performed Train-Test Split  
- Applied Multiple Linear Regression  
- Evaluated using **R² Score**

### 4️⃣ Deployment
- Serialized model using `pickle`  
- Built a Streamlit app for live predictions  

---

## 📊 Model Performance

**R² Score: ~0.62**

The model explains a meaningful portion of price variance while leaving room for future improvements through advanced techniques and larger datasets.

---

## 🖥️ Demo

![App Screenshot](screenshots/home.png)

### Home Interface
![Home](screenshots/home.png)

### Prediction Example
![Prediction](screenshots/prediction.png)

---

## ▶️ Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/car-price-prediction.git

# Navigate into the project
cd car-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## 🎯 What I Learned

- Regression modeling  
- Feature engineering  
- Handling categorical data  
- Model serialization  
- Deploying ML applications  
- Building user-focused interfaces  

---

## 🚀 Future Improvements

- Experiment with advanced regression models  
- Perform hyperparameter tuning  
- Deploy on cloud platforms  
- Improve accuracy with larger datasets  

---

## 👨‍💻 Author

**Anuj Kumar**  
AIML Undergraduate focused on building practical Machine Learning projects.

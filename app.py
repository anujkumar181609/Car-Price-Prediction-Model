import streamlit as st 
import pandas as pd
import pickle
from datetime import datetime
from pathlib import Path

#importing dataset
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "car_price.csv"
df = pd.read_csv(csv_path)

#importing model
model_path = BASE_DIR / "car_price_model.pkl"
model = pickle.load(open(model_path, 'rb'))

#heading
st.title("Car Price Prediction Model")

#entries
company =st.selectbox("Company",df['company'].unique())
filtered_models= df[df['company']==company]['name'].unique()

name= st.selectbox("Car Model",filtered_models)

year= st.slider("Year",1995,2024)

kms= st.number_input("KMs Driven")

filtered_fuels= df[(df['company']== company ) & (df['name']==name)]['fuel_type'].unique()
fuel= st.selectbox("Fuel Type", filtered_fuels)


if st.button("Predict Price"):
    
    curr_year= datetime.now().year
    car_age= curr_year-year
    
    input_df= pd.DataFrame(
        [[name, company, car_age, kms, fuel]],
        columns=['name', 'company','car_age','kms_driven','fuel_type']
    )
    
    prediction=model.predict(input_df).item()
    
    st.success(f"Estimated Price: ₹ {round(prediction,2)}")

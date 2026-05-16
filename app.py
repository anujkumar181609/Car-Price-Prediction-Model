import streamlit as st 
import pandas as pd
import pickle
from datetime import datetime

#importing dataset
df= pd.read_csv('car_price.csv')

#importing model
model= pickle.load(open('car_price_model.pkl','rb'))

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
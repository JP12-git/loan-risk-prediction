import streamlit as st
import joblib
import pandas as pd

model = joblib.load('loan_risk_prediction_model.pkl')
feature = joblib.load('features.pkl')

st.set_page_config(page_title='Loan Risk Prediction',layout='centered',initial_sidebar_state='expanded')
st.title("🏦 Loan Risk Prediction 💰")
st.write(' 📝 Enter The Candidate Information Below ⤵️')

numeric_col = ['Income','LoanAmount','CreditScore','YearsExperience']

selectbox_col = {
    'Education':['High School','Bachelors','Masters','PhD'],
    'Gender':['Male','Female'],
    'EmploymentType':['Self-Employed','Salaried','Unemployed']
}

user = {}

for col in feature :

    if col in numeric_col :

        user[col] = st.number_input(col,value=None,placeholder='Enter Here')

    elif col in selectbox_col :

        user[col] = st.selectbox('Select Value',selectbox_col[col]) 

    else :

        user[col] = st.text_input(f'Enter {col}')

Input = pd.DataFrame([user])
st.subheader(" 🗒️ User Input")
st.dataframe(Input)

if st.button(" 🔮 Predict Loan Status 🕹️") :
    Pred = model.predict(Input)
    st.subheader(" 🎯 Result ")

    if Pred[0]=="Approved":
        st.success(" 🟩 ✅ Loan Approved")
    elif Pred[0]=="Rejected":
        st.error(" 🟥 ❌ Loan Rejected")

st.markdown("""<div style ="text-align: right; 
font-family: Constantia; 
font-style: italic; 
font-weight: bold ; 
font-size: 20px; 
color:gray ;">
Developed by Prerak Jasani 
</div>""", unsafe_allow_html=True)       
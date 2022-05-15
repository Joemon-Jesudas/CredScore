import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput
import model
import joblib
import os
import numpy as np

st.set_page_config(page_title="CredScore Calculator",
                   page_icon="📵", layout="wide")

curr_path = os.path.dirname(os.path.realpath(__file__))

feature_cols = joblib.load(curr_path + "/features.joblib")

with st.form("prediction_form"):
    st.header("Enter the Details to calulate credit Risk")

    Credit_Amount = st.number_input("Enter Credit Amount: ",value=0, format="%d")
    Age = st.number_input("Age: ", value=0, format="%d")
    Duration = st.number_input("Duration(in Months): ", value=0, format="%d")
    Installment_rate = st.number_input("Enter the installment rate: ")
    Install_plans=st.number_input("Enter the installment Plan(0-2): ",value=0,format="%d")
    Checking_Account = st.number_input("Enter the checking account type(0-3):", value=0, format="%d")
    Savings_Account = st.number_input("Enter the Savings account type(0-4):", value=0, format="%d")
    Purpose=st.number_input("Enter purpose of Loan Amount(0-9): ", value=0, format="%d")
    No_of_credits=st.number_input("Enter No of credits(1-4):", value=0, format="%d")
    Employement = st.number_input("Enter Employement type(0-4):", value=0, format="%d")
    Credit_History=st.number_input("Enter Credit history (0-4):", value=0, format="%d")
    Deb_gran=st.number_input("Debtor/Guarantors (0-2):", value=0, format="%d")
    sex=st.number_input("Enter Sex (0-1):", value=0, format="%d")
    Housing=st.number_input("Enter Housing Type (0-2):", value=0, format="%d")
    Job_type =st.number_input("Enter Job Type (0-3):", value=0, format="%d")
    Foreigner = st.number_input("Enter Foreigner/not (0-1):", value=0, format="%d")
    Property = st.number_input("Enter Property type (0-3):", value=0, format="%d")

    submit_val = st.form_submit_button("Predict Credit Risk")

if submit_val:
    attributes = np.array([Checking_Account,Duration,Purpose,Credit_Amount,No_of_credits,Employement,Savings_Account,
                           Deb_gran,Credit_History,Installment_rate,Install_plans,sex,Age,Housing,Job_type,Property,Foreigner])
    print("attributes value")
    status = model.predict(attributes.reshape(1, -1))
    if status:
        st.error("Bad Credit Rating")
    else:
        st.success("Good Credit Rating")
        st.balloons()
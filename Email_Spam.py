import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from PIL import Image

model = pickle.load(open(r"C:\Users\RAGHAVENDRA KUMAR\ML\NLP\Email_spam_ham.pkl","rb"))
# Display the image
#st.image(image, use_column_width=True)
st.title("Email Spam or Ham ML Project")
st.subheader("By Patwari Raghottam")
email=st.text_input("Enter the Email : ")
if st.button("Submit"):
    data = model.predict([[email]])[0]
    st.write("The Email is",data,'minutes')

import pandas as pd
from modelpredict import prediction
import streamlit as st
import numpy as np
def main():
    st.title("Credit Card Default Prediction App")
    pred=prediction()
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your data here", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("Input Data")
        st.write(data)
        if st.button("Predict"):
            result = pred.predictionFromModel(data)
            st.subheader("Predictions")
            st.write("File stored at:", result)
    else:
        st.subheader("Please upload a CSV file")
if __name__ == '__main__':
    main()

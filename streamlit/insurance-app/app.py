from pycaret.regression import load_model, predict_model
import streamlit as streamlit
import pandas as pd
import numpy as np

model = load_model('deployment_01012021')

def predict(model, inpput_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'];0'
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo.png')
    image_hospital = Image.open('hospital.jpg')
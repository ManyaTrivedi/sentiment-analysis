import streamlit as st
import tensorflow as tf
import os
from tensorflow.keras.models import load_model
from Untitled import predict_sentiment #as pred 
# from Untitled  

def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL ### Whatever not coming in negative and positive sentiments has been considered as neutral
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def predict_sentiment(text):
    # Preprocess the input sentence
    text = tf.keras.preprocessing.text.text_to_word_sequence(text)
    text = tf.keras.preprocessing.sequence.pad_sequences([text], maxlen=50)
    # Use the model to predict sentiment
    sentiment = sentiment_model.predict(text)
    sentiment = "Positive" if sentiment > 0.5 else "Negative"
    return sentiment
sentiment_model2 = load_model(r'C:\\Users\\riddh\\Desktop\\hackathon\\model.w2v')

st.title("Sentiment Analysis App")
text = st.text_area("Enter your text here")

sentiment_model1 = load_model(r'C/Users/riddh/Desktop/hackathon/model.h5')
if st.button("Analyze"):
    senti=predict_sentiment(text)
    st.write("sentiment ",senti)
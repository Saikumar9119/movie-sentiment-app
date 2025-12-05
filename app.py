import streamlit as st
import joblib
import numpy as np

# Load vectorizer and model once
@st.cache_resource
def load_artifacts():
    vectorizer = joblib.load("models/tfidf_vectorizer.joblib")
    model = joblib.load("models/sentiment_model.joblib")
    return vectorizer, model

vectorizer, model = load_artifacts()

# Predict sentiment from raw text
def predict_sentiment(text):
    X = vectorizer.transform([text])
    
    # If the model provides probabilities
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X)[0]
        idx = np.argmax(proba)
        label = model.classes_[idx]
        confidence = proba[idx]
        return label, confidence
    
    # Fallback for models without probability support
    label = model.predict(X)[0]
    return label, None

# Streamlit UI
st.title("Movie Review Sentiment Analysis")
st.write("Enter a movie review and get its predicted sentiment.")

# Text input box
review_text = st.text_area("Write your review here:", height=200)

# Prediction button
if st.button("Predict"):
    if not review_text.strip():
        st.warning("Please enter some text.")
    else:
        label, confidence = predict_sentiment(review_text)
        sentiment = "Positive" if label == "pos" else "Negative"
        
        st.subheader(f"Sentiment: {sentiment}")
        
        if confidence is not None:
            st.write(f"Confidence: {confidence:.2f}")

import streamlit as st
import joblib

# Load Model and TF-IDF Vectorizer
model = joblib.load("emotion_model.joblib")
tfidf = joblib.load("tfidf.joblib")

# Emotion Mapping
emotion_labels = {
    0: "Sadness 😔",
    1: "Anger 😠",
    2: "Love ❤️",
    3: "Surprise 😲",
    4: "Fear 😨",
    5: "Joy 😊"
}

# Page Configuration
st.set_page_config(
    page_title="EmotionSense",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 EmotionSense")
st.subheader("AI-Powered Emotion Detection using NLP")

st.markdown("""
Enter any sentence or paragraph and the model will predict the underlying emotion.

**Model:** Logistic Regression  
**Vectorization:** TF-IDF  
**Accuracy:** 86.12%
""")

# Text Input
user_text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Example: I am feeling very happy today because I achieved my goal."
)

# Prediction Button
if st.button("Predict Emotion"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        transformed_text = tfidf.transform([user_text])

        prediction = model.predict(transformed_text)[0]

        st.success(
            f"Predicted Emotion: {emotion_labels[prediction]}"
        )

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using Streamlit, TF-IDF and Logistic Regression"
)
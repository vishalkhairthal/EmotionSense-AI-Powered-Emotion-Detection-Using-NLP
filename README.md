EmotionSense: AI-Powered Emotion Detection Using NLP
EmotionSense is a Natural Language Processing (NLP) project that analyzes user-provided text and predicts the underlying emotion. The model is trained using TF-IDF feature extraction and Logistic Regression, achieving an accuracy of 86.12% on the test dataset.
The application provides a simple and interactive Streamlit-based user interface where users can enter text and instantly receive emotion predictions.
Features
Text Emotion Classification
TF-IDF Feature Extraction
Logistic Regression Model
Streamlit Interactive UI
Real-Time Predictions
Six Emotion Categories:
Sadness
Anger
Love
Surprise
Fear
Joy
Tech Stack
Python
Pandas
NumPy
Scikit-Learn
TF-IDF Vectorizer
Logistic Regression
Joblib
Streamlit
Model Performance
Algorithm: Logistic Regression
Feature Extraction: TF-IDF
Accuracy: 86.12%
Project Structure
EmotionSense/
│
├── app.py
├── emotion_model.joblib
├── tfidf.joblib
├── requirements.txt
├── README.md

Future Improvements
Emotion probability scores
Confidence visualization
Deep Learning (LSTM/BERT) implementation
Emotion trend analytics
Multi-language support

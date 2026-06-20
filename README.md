# 🧠 EmotionSense: AI-Powered Emotion Detection Using NLP

EmotionSense is a Natural Language Processing (NLP) project that predicts human emotions from text using Machine Learning. The model analyzes user input and classifies it into one of six emotions: Sadness, Anger, Love, Surprise, Fear, or Joy.

The project uses TF-IDF Vectorization for feature extraction and Logistic Regression for classification, achieving an accuracy of **86.12%**.

---

## 🚀 Features

- Emotion Detection from Text
- TF-IDF Feature Extraction
- Logistic Regression Classification
- Interactive Streamlit Web Application
- Real-Time Emotion Prediction
- Clean and User-Friendly Interface

---

## 🎯 Supported Emotions

- Sadness 😔
- Anger 😠
- Love ❤️
- Surprise 😲
- Fear 😨
- Joy 😊

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- Streamlit

---

## 📊 Model Performance

| Model | Accuracy |
|---------|----------|
| Logistic Regression + TF-IDF | 86.12% |

---

## 📁 Project Structure

```text
Emotions/
│
├── app.py
├── emotion_model.joblib
├── tfidf.joblib
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/EmotionSense.git
```

Move into the project directory:

```bash
cd EmotionSense
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🖥️ Example Input

```text
I am feeling very happy today because I achieved my goal.
```

### Prediction

```text
Joy 😊
```

---

## 🔮 Future Improvements

- Emotion Probability Scores
- Confidence Visualization
- Deep Learning Models (LSTM, BERT)
- Multi-Language Emotion Detection
- Advanced NLP Preprocessing

---

## 👨‍💻 Author

**Vishal Gupta**

B.Tech Computer Science Engineering Student  
Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star!

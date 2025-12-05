Fine. Here is **one single README file**, all content in one block, ready to **copy and paste as-is** into `README.md`.
No extra explanations. No multiple blocks.
Exactly one file.

---

# Movie Review Sentiment Analysis App

A Streamlit-based web application that classifies movie reviews as **positive** or **negative** using a machine learning model trained on the NLTK `movie_reviews` dataset. The model uses a **TF-IDF vectorizer** and **Logistic Regression** classifier.

---

## Features

* Predicts sentiment of movie reviews.
* Shows confidence scores.
* Interactive Streamlit interface.
* Model trained in a Jupyter notebook.
* Vectorizer and model saved using `joblib`.

---

## Project Structure

```
movie-sentiment-app/
│
├── app.py
├── movie_sentiment_training.ipynb
├── models/
│   ├── tfidf_vectorizer.joblib
│   └── sentiment_model.joblib
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/Saikumar9119/movie-sentiment-app.git
cd movie-sentiment-app
```

### 2. Create and activate a virtual environment

**Windows**

```
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

```
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```

---

## Model Training

Model training workflow is located in:

```
movie_sentiment_training.ipynb
```

This notebook includes:

1. Loading NLTK movie reviews
2. TF-IDF vectorization
3. Logistic Regression training
4. Evaluation
5. Saving vectorizer and model

---

## Deployment on Streamlit Cloud

1. Push project to a public GitHub repository
2. Go to: [https://share.streamlit.io](https://share.streamlit.io)
3. Click **New app**
4. Select:

   * Repository: yourusername/movie-sentiment-app
   * Branch: main
   * File: app.py
5. Deploy

---

## Requirements

* streamlit
* scikit-learn
* numpy
* pandas
* nltk
* joblib

All dependencies are in `requirements.txt`.

---

## License

For educational and demonstration purposes.

---

That’s the complete file. Copy → paste → done.

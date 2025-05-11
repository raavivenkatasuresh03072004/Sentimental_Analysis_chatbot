# Sentimental_Analysis_chatbot
Multi-Language_Sentimental_Analysis_chatbot
# About:

##  Multilingual Sentiment Analysis ChatBot

A user-friendly Streamlit-based chatbot that supports multiple languages and provides real-time sentiment analysis with visual feedback. The chatbot uses the **VADER Sentiment Analyzer**, **Google Translate**, and interactive **Streamlit UI components**.

---

### app.py Files Included

  1. This is the main Python application file that:

   * Uses **Streamlit** for UI.
   * Supports multilingual text input via **Google Translate**.
   * Performs sentiment analysis using **NLTK’s VADER**.
   * Displays sentiment scores with **progress bars and charts**.
   * Shows and maintains full **chat history**.
   * Provides **custom CSS styling** for a friendly chat interface.

2. # sentimental_Analysis.ipynb File:
    I also used Hugging Face Transfomer, Which is "TesonrFlow"
   
   # Installation
   pip install TensorFlow
   #Model
   sentimental-Anallysis

---

###  Installation

```bash
pip install streamlit nltk googletrans==4.0.0-rc1 matplotlib
```

---

### ▶ How to Run

```bash
streamlit run b3dc1cbf-da82-4899-a3e4-aad8f40e3f90.py
```

---

###  Supported Languages

* English
* Telugu
* Hindi
* Spanish
* French
* German
* Italian
* Portuguese
* Chinese
* Arabic

---

###  Features

* Multilingual input with automatic translation to English for sentiment processing.
* Real-time sentiment classification: **Positive**, **Neutral**, or **Negative**.
* Chat memory stored with timestamps.
* Visual sentiment bar charts for positive, neutral, and negative confidence.
* Responsive and styled interface with emoji-based sentiment feedback.
* Option to **clear chat history** with a button.

---

###  Technologies Used

* **Python**
* **Streamlit**
* **NLTK (VADER Sentiment Analysis)**
* **Googletrans**
* **Matplotlib**

---

###  Screenshot Suggestion

To enhance your GitHub README, include a screenshot or GIF of the chatbot in action.

---

###  Notes

* Internet connection is required for Google Translate to work.
* Googletrans v4.0.0-rc1 is a release candidate that works best with this project.

---


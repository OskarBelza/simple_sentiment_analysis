# Sentiment Analysis App

This project is a **Sentiment Analysis Web App** built using **Streamlit** and **Natural Language Processing (NLP)** techniques. It translates input text into English and analyzes its sentiment using **VADER Sentiment Analysis** from **NLTK**.

## Features
- **Text Translation**: Automatically translates input text to English using the `translators` library.
- **Sentiment Analysis**: Uses **VADER Sentiment Analysis** to determine if the text is **positive, negative, or neutral**.
- **Interactive Web Interface**: Built with **Streamlit** for an easy-to-use UI.

## Installation

### **1. Install Python Dependencies**
Ensure you have Python installed, then install the required packages using:
```sh
pip install streamlit nltk translators
```

### **2. Download NLTK Data**
Run the following command to download the necessary **VADER** sentiment analysis model:
```python
import nltk
nltk.download('vader_lexicon')
```

## Usage

### **Run the App**
To launch the sentiment analysis app, run:
```sh
streamlit run app.py
```
This will open a web browser with the sentiment analysis tool.

### **How It Works?**
1. **User inputs text** in any language.
2. **Text is translated** to English using `translators`.
3. **Sentiment Analysis** is performed using `SentimentIntensityAnalyzer`.
4. **Results are displayed** as a sentiment score:
   - **Positive** (score > 0)
   - **Negative** (score < 0)
   - **Neutral** (score = 0)

## Example Output
```
Wynik analizy sentymentu: 0.75
To pozytywny tekst!
```

## File Structure
```
SentimentApp/
│── app.py          # Main Streamlit application
│── README.md       # Documentation
```

## License
This project is open-source and available under the **MIT License**.

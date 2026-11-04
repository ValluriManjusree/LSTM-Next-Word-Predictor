# LSTM Next Word Predictor

## Project Overview
The LSTM Next Word Predictor is a web-based application that predicts the next word based on the text entered by the user. It uses a Long Short-Term Memory (LSTM) neural network to learn word sequences and generate predictions.

## Objectives
- To develop a next-word prediction system using deep learning.
- To understand sequential data processing using LSTM.
- To build a simple interactive web application for text prediction.

## Technologies Used
- Python
- TensorFlow / Keras
- LSTM (Long Short-Term Memory)
- Flask
- HTML
- CSS
- JavaScript

## Model Architecture
1. Input Text
2. Tokenization
3. Embedding Layer
4. LSTM Layer
5. Dense Layer
6. Softmax Activation
7. Next Word Prediction

## Project Structure
```text
LSTM-Next-Word-Predictor/
├── app.py
├── requirements.txt
├── next_word_lstm.keras
├── tokenizer.pkl
├── max_sequence_len.pkl
├── templates/
│   └── index.html
└── static/
    ├── app.js
    └── style.css
```

## How It Works
1. The user enters a sequence of words.
2. The input text is converted into numerical tokens.
3. The trained LSTM model processes the sequence.
4. The model predicts the next word.
5. The predicted word is displayed on the website.

## Installation and Execution

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open the local URL displayed in the terminal in your web browser.

## Future Enhancements
- Improve prediction accuracy with larger datasets.
- Support longer text sequences.
- Enhance the user interface.
- Explore more advanced language models.

## Author
**Valluri Manjusree**

B.Tech – Computer Science and Engineering

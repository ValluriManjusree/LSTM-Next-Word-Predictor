
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained LSTM model
model = tf.keras.models.load_model("next_word_lstm.keras")

# Load the tokenizer
with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

# Load the sequence length
with open("max_sequence_len.pkl", "rb") as file:
    max_sequence_len = pickle.load(file)


def predict_next_word(seed_text):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]

    if not token_list:
        return "No known words found. Try different text."

    token_list = token_list[-(max_sequence_len - 1):]

    token_list = tf.keras.utils.pad_sequences(
        [token_list],
        maxlen=max_sequence_len - 1,
        padding="pre"
    )

    predictions = model.predict(token_list, verbose=0)
    predicted_id = int(np.argmax(predictions, axis=1)[0])

    for word, index in tokenizer.word_index.items():
        if index == predicted_id:
            return word

    return "No prediction available."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    input_text = data.get("text", "").strip()

    if not input_text:
        return jsonify({"prediction": "Please enter some text."}), 400

    prediction = predict_next_word(input_text)

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)


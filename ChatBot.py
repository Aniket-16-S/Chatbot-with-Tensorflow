import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import json
import numpy as np
import tensorflow as tf
import random
import nltk
from nltk.stem import LancasterStemmer
from sys import exit

stemmer = LancasterStemmer()
nltk.download('punkt')

# Load intents
try:
    with open("faq.json", "r") as file:
        intents = json.load(file)
except FileNotFoundError:
    print("faq.json not found. Provide valid data.")
    exit(0)

# Preprocessing
words, classes, documents = [], [], []
ignore_words = ["?", "!", ".", ","]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = sorted(set([stemmer.stem(w.lower()) for w in words if w not in ignore_words]))
classes = sorted(set(classes))

# Build training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = [1 if w in [stemmer.stem(word.lower()) for word in doc[0]] else 0 for w in words]
    output_row = output_empty.copy()
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
train_x, train_y = zip(*training)
train_x, train_y = np.array(train_x), np.array(train_y)

# Model training function
def train_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(len(train_y[0]), activation="softmax")
    ])
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(train_x, train_y, epochs=200, batch_size=8, verbose=1)
    model.save("chatbot_model.keras")
    return model

# Load or train model
try:
    model = tf.keras.models.load_model("chatbot_model.keras")
    if model.input_shape[1] != len(train_x[0]):
        print("Model input shape mismatch. Retraining...")
        model = train_model()
except Exception:
    model = train_model()

# Sentence → BoW
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return [1 if w in sentence_words else 0 for w in words]

# Classify intent
def classify(sentence):
    bow = np.array([clean_up_sentence(sentence)])
    prediction = model.predict(bow, verbose=0)[0]
    ERROR_THRESHOLD = 0.6
    results = [[i, p] for i, p in enumerate(prediction) if p > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [(classes[r[0]], r[1]) for r in results]

# Generate response
def chatbot_response(text):
    intents_detected = classify(text)
    if intents_detected:
        intent_tag = intents_detected[0][0]
        for intent in intents["intents"]:
            if intent["tag"] == intent_tag:
                return random.choice(intent["responses"])
    return "I'm sorry, I couldn't understand."

# For API or CLI usage
def ask(query: str = None):
    if query is None:
        return "Query can't be None."
    return chatbot_response(query.lower())

# CLI interface
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Chatbot:", chatbot_response(user_input))

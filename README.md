# Chatbot with TensorFlow

*Your intelligent conversational assistant, powered by TensorFlow neural network and designed for easy customization.*
--
## Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Cloning the Repository](#cloning-the-repository)
    * [Installation](#installation)
    * [Running the Chatbot](#running-the-chatbot-server)
    * [Using the Dashboard](#using-the-dashboard)
* [How it Works](#how-it-works)
* [Customizing and Training](#customizing-and-training)
* [Contributing](#contributing)

## About the Project

This project provides a robust and flexible chatbot solution built with `TensorFlow` and Natural Language Toolkit (`NLTK`) for `natural language processing`.
It's designed to be easily trainable with your custom FAQ data,making it ideal for small-scale businesses or anyone needing a simple, self-trainable conversational AI for their website or application.
The system includes a `FastAPI` server for seamless API interaction and a Streamlit dashboard for managing unanswered queries.

## Features

* **TensorFlow-Powered NLP :** Utilizes a feedforward neural network for efficient and accurate intent classification.
* **Customizable Training Data :** Easily train the chatbot with your own JSON-formatted question-answer pairs without modifying core code.
* **FastAPI Integration :** Provides a high-performance `RESTful API` for sending queries and receiving chatbot responses.
* **Streamlit Dashboard :** A user-friendly web interface to review and answer previously unrecognized queries, improving the chatbot's knowledge base.
* **Scalable & Simple :** Designed for straightforward deployment and management, suitable for various small-scale applications.

## Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **RESTful API**
* **NLTK (Natural Language Toolkit)**
* **FastAPI**
* **Pydantic**
* **Streamlit**

## Project Structure

* `dashboard.py`: Contains the Streamlit application for managing unanswered queries.
* `ChatBot.py`: Core chatbot logic, including NLP preprocessing, TensorFlow model definition, training, and prediction.
* `main.py`: Sets up and runs the FastAPI server for the chatbot API.
* `faq.json`: Contains training data of your chatbot.
* `models/`: Saves a trained model for fast startup time.
* `requirements.txt`: (Will list all necessary Python dependencies)

## Getting Started

Follow these steps to get your chatbot up and running.

### Prerequisites

Ensure you have Python 3.9+ installed on your system. (3.12 recommended)
It's recommended to use a virtual environment.

### Cloning the Repository

```bash
git clone https://github.com/Aniket-16-S/Chatbot-with-Tensorflow.git
```
change cwd
```bash
cd Chatbot-with-Tensorflow)
```
### Installation

It's highly recommended to create and activate a virtual environment before installing dependencies:

Install the required packages :
```bash
pip install -r requirements.txt
```
### Running the Chatbot
Running in CLI for chatting
```bash
python ChatBot.py
```
Running the Chatbot ( Server only )
```bash
python main.py
```
This will typically start the FastAPI server at `http://127.0.0.1:8000`. You can then interact with the chatbot via its API (e.g., using POST requests to send queries).
Goto following url for testing the server
```bsah
http://127.0.0.1:8000/docs
```
Using the Dashboard
To manage unanswered queries, run the Streamlit dashboard:
```bash
streamlit run dashboard.py
```
This will open the dashboard in your web browser, usually at `http://localhost:8501`

## How it Works
The chatbot uses a deep learning model to classify user intents. When a query is received:

- **Preprocessing** : NLTK is used to tokenize and stem the input query.
- **Vectorization** : The preprocessed query is converted into a numerical representation (bag of words).
- **Prediction** : The TensorFlow model predicts the intent (tag) of the query.
- **Response** : A predefined response associated with the predicted intent is returned.

The core TensorFlow model architecture :
This is a ***feedforward neural network*** *( F N N )*, also known as a *Multi-Layer Perceptron* (MLP), built with TensorFlow/Keras.

## Key characteristics:

- **Architecture** : It has two hidden layers with ReLU activation, each followed by a dropout layer for regularization (to prevent overfitting). The output layer uses a softmax activation function, typical for multi-class classification.
- **Input** : It takes a numerical input (likely a bag-of-words or TF-IDF representation of text) with a dimension equal to len(train_x[0]).
- **Output** : It outputs probabilities for len(train_y[0]) different classes (intents).
- **Training** : It's compiled with categorical_crossentropy loss (suitable for multi-class classification where outputs are one-hot encoded), optimized using the Adam algorithm, and trained for 200 epochs with a batch size of 8.

## Contributing
We welcome contributions to make this chatbot even better! If you have suggestions, bug reports, or want to contribute code, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature-name).
- Make your changes and commit them (git commit -m 'Add new feature').
- Push to your branch (git push origin feature/your-feature-name).
- Open a Pull Request (PR) to the main branch of this repository.
- Please ensure your code adheres to good practices and includes relevant documentation or comments.

## Other Projects 
Please feel free to check out my other projects. [GitHub profile](https://github.com/Aniket-16-S)

# Sentiment Analysis

## Overview
This project performs sentiment analysis on text data, classifying sentiments as positive, negative, or neutral.
## Model Details
-**Training Data:** Labeled sentiment dataset (TweetEval (sentiment)) </br>
-**Metrics:** Accuracy, F1-score
- Model: [SenbiModel](https://huggingface.co/akdfga/SenbiModel)
- Tokenizer: [Tokenizer](https://huggingface.co/akdfga/tokenizer)


## Features
- Text preprocessing (data cleaning, tokenization)
- Sentiment classification (positive, negative, neutral)
- Visualization of sentiment distribution and model perfomance
- Web interface

## Technologies Used
- Python
- transformer-based language pre-trained model RoBERTa
- scikit-learn
- PyTorch
- pandas & numpy

## Installation
Clone the repository and install the required dependencies:
```sh
# Clone the repository
git clone https://github.com/NURnurNURnurNUR/Sentiment-Analysis.git
cd Sentiment-Analysis
```

### Running the Gradio Application
To launch the interactive web interface using Gradio, run:
```sh
python gradio_application.py
```
This will start a local web server where users can input text and receive real time sentiment predictions.

## Code Structure
```
│-- SenbiAI.ipynb #model
|-- gradio_application.py #script for web interface
|-- push.py #script for pushing model and tokenizer to Hugging Face 
│-- checkpoint_performance.png  # Graph of model perfomance
│-- .gitignore          # Files and directories to ignore
│-- README.md           # Documentation
```

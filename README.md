# Sentiment Analysis Application

## Overview
The Sentiment Analysis Application is a Python-based tool designed to analyze customer feedback and classify it as positive, negative, or neutral. It uses machine learning models to perform sentiment analysis, providing an intuitive graphical user interface (GUI) for easy interaction.

---

## Features
- **Tkinter-based GUI**: A user-friendly interface to input and analyze text.
- **Machine Learning Model**: Utilizes pre-trained models for accurate sentiment classification.
- **Data Visualization**: Includes visual representations of sentiment trends.

---

## Requirements
To run the application, ensure the following are installed:

- **Python**: Version 3.8 or higher.
- **Python Libraries**:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `joblib`
  - `graphviz`

---

## Installation

1. **Download and Install Python**:
   Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/).

2. **Install Required Libraries**:
   Use the following command to install all required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn joblib graphviz
    ```
3. **Download Application Files**:
   - Clone or download this repository.
   - Ensure the following files are in a local directory:
     - `main.ipynb`
     - `GUI.py`
     - `sentiment_model.pkl`
     - `vectorizer.pkl`
     - Dataset folder (`dataset/`)

---

## Usage

1. **Run the Application**:
   Execute the GUI application by running the following command in your terminal or command prompt:
   ```bash
   python GUI.py
    ```
2. **Analyze Sentiments**:
   - Enter a sentence or customer feedback in the input text box of the GUI.
   - Click the "Analyze" button to view the sentiment classification.

---

## File Descriptions
- `main.ipynb`: Jupyter Notebook for exploratory data analysis and model training.
- `GUI.py`: Python script to launch the GUI for sentiment analysis.
- `sentiment_model.pkl`: Pre-trained machine learning model for sentiment classification.
- `vectorizer.pkl`: Vectorizer used to preprocess and transform input text.
- `dataset/`: Directory containing training and testing data for the model.

---

## Project Structure
```
Sentimen-Analysis-Application
├── application
│   ├── dataset
│   ├── decision_tree.png
│   ├── GUI.py
│   ├── main.ipynb
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
└── README.md
```

---

## License
MIT License

Copyright (c) 2024 Benjamin Anderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


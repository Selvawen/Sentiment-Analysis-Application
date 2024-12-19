import tkinter as tk
from tkinter import messagebox
import joblib

model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    import re
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

def predict_sentiment_gui():
    feedback = input_text.get("1.0", "end").strip()
    if not feedback:
        messagebox.showerror("Input Error", "Please enter some feedback text.")
        return
    
    feedback_cleaned = clean_text(feedback)
    feedback_vectorized = vectorizer.transform([feedback_cleaned])
    prediction = model.predict(feedback_vectorized)
    
    sentiment = "Positive"
    if prediction[0] == 0:
        sentiment = "Negative"
    messagebox.showinfo("Sentiment Analysis Result", f"Predicted Sentiment: {sentiment}")

app = tk.Tk()
app.title("Sentiment Analysis Application")
app.geometry("400x300")
tk.Label(app, text="Enter customer feedback:", font=("Arial", 12)).pack(pady=10)
input_text = tk.Text(app, height=5, width=40, font=("Arial", 12))
input_text.pack(pady=10)
analyze_button = tk.Button(app, text="Analyze Sentiment", font=("Arial", 12), command=predict_sentiment_gui)
analyze_button.pack(pady=10)
app.mainloop()
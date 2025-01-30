import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
import requests
import spacy
nlp = spacy.load("en_core_web_sm")
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt

# Data cleaning
def clean_data(data):
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the 'age' column exists, and if not, process the existing columns
    print("DataFrame columns:", df.columns)

    # Clean data (remove rows with missing 'title' or 'body', if needed)
    df.dropna(subset=['title', 'body'], inplace=True)
    
    # You can apply some other cleaning logic depending on the data, like removing empty titles or filtering content
    # For example, filtering based on 'userId' if needed
    df = df[df['userId'] > 0]  # Example of filtering based on the 'userId'

    return df



# AI prediction
def ai_prediction(data):
    # Example of making a simple prediction based on available 'id' column
    if 'id' in data.columns:
        # Let's assume we're making a simple prediction using 'id' (for example)
        prediction = data['id'].mean()  # Simple mean of 'id' as a placeholder prediction
        return prediction
    return "No valid data available for prediction"



# API call for fetching external data
def fetch_api_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()

# Chatbot
def chatbot_response(user_input):
    doc = nlp(user_input)
    # For simplicity, we'll just respond to greetings and general questions
    if "hello" in doc.text.lower():
        return "Hi there! How can I help you today?"
    elif "how are you" in doc.text.lower():
        return "I'm doing well, thanks for asking!"
    elif "bye" in doc.text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."


# View function for the home page
def index(request):
    # Fetch external API data
    api_data = fetch_api_data()

    # Process and clean the data
    cleaned_data = clean_data(api_data)

    # Make an AI prediction
    prediction = ai_prediction(cleaned_data)

    return render(request, 'core/index.html', {'prediction': prediction})

# View function for chatbot
def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chatbot_response(user_input)
        return render(request, 'core/chatbot.html', {'response': response})
    return render(request, 'core/chatbot.html')

# View function for data visualization
def api_data_visualization(request):
    # Example of fetching and cleaning data (replace with your actual data)
    data = fetch_api_data()
    df = pd.DataFrame(data)
    
    # Create a simple chart
    fig, ax = plt.subplots()
    ax.bar(df['id'], df['userId'])  # Modify according to your actual data

    # Ensure plotting is done on the main thread
    plt.show()
    return render(request, 'core/api_data_visualization.html', {'data': data})

import threading

def plot_on_main_thread():
    data = fetch_api_data()
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.bar(df['id'], df['userId'])  # Adjust according to your data
    plt.show()

# Run the plot function on the main thread
threading.Thread(target=plot_on_main_thread).start()

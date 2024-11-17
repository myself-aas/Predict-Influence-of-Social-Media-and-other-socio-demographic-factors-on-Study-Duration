# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('study_duration_model.pkl')

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from form
    data = request.form
    input_data = pd.DataFrame({
        'SSC_GPA': [float(data['SSC_GPA'])],
        'HSC_GPA': [float(data['HSC_GPA'])],
        'Residence': [int(data['Residence'])],
        'Family_Education': [int(data['Family_Education'])],
        'Social_Media_Engagement': [int(data['Social_Media_Engagement'])],
        'Relationship': [int(data['Relationship'])],
        'Bad_Habits': [int(data['Bad_Habits'])],
        'Politics': [int(data['Politics'])],
        'External_Factors': [int(data['External_Factors'])]
    })

    # Make prediction
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    # Return the result as JSON
    return jsonify({'predicted_study_duration': f"{output} hours"})

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

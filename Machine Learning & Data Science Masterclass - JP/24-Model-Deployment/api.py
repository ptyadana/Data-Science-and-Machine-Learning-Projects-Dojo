from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask App
app = Flask(__name__)

# Connect POST API CALL => predict () function    http://localhost:5000/predict
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON request
    feature_data = request.json
    
    # Convert JSON to Pandas DF (column names)
    df = pd.DataFrame(feature_data)
    df = df.reindex(columns=column_names)
    
    # Predict and Return predictions
    predictions = list(model.predict(df))
    
    return jsonify({'prediction': str(predictions)})# Prediction

# Load the model and load the columns
if __name__=='__main__':
    model = joblib.load('Model/final_model.pkl')
    column_names = joblib.load('Model/columns_names.pkl')
    
    app.run(debug=True)

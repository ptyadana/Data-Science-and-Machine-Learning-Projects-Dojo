from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
import joblib


#### THIS IS WHAT WE DO IN POSTMAN ###
# STEP 1: Create New Request
# STEP 2: Select POST
# STEP 3: Type correct URL (http://127.0.0.1:5000/api/flower)
# STEP 4: Select Body
# STEP 5: Select JSON
# STEP 6: Type or Paste in example json request
# STEP 7: Run 02-Basic-API.py to launch server and confirm the site is running
# Step 8: Run API request


#---------  prediction function --------------
def return_prediction(model, scaler, sample_json):
    sepal_length = sample_json['sepal_length']
    sepal_width = sample_json['sepal_width']
    petal_length = sample_json['petal_length']
    petal_width = sample_json['petal_width']
    
    flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    classes = np.array(['setosa', 'versicolor', 'virginica'])
    
    flower = scaler.transform(flower)
    
    class_index = np.argmax(model.predict(flower), axis=-1)[0]
    
    return classes[class_index]


#--------- Flask App ------------
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flask App is running :)</h1>'

# load model and scaler
iris_model = load_model('../Models/final_iris_model.h5')
iris_scaler = joblib.load('../Models/iris_scaler.pkl')

@app.route('/api/flower', methods=['POST'])
def predict_flower():
    print(request.json)
    content = request.json
    results = return_prediction(iris_model, iris_scaler, content)
    return jsonify(results)
    

if __name__ == '__main__':
    app.run()
from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the trained decision tree model
model = joblib.load("decision_tree_model.pkl")


@app.route('/data', methods=['POST'])


def predict():
    data = request.json
    outlook = data["outlook"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    wind = data["wind"]
    
    # Convert categorical features to numerical values using mapping dictionaries
    outlook_map = {"sunny": 0, "overcast": 1, "rain": 2}
    temperature_map = {"hot": 0, "mild": 1, "cool": 2}
    humidity_map = {"high": 0, "normal": 1}
    wind_map = {"weak": 0, "strong": 1}
    
    
    outlook = outlook_map[outlook]
    temperature = temperature_map[temperature]
    humidity = humidity_map[humidity]
    wind = wind_map[wind]
    
    prediction = model.predict([[outlook, temperature, humidity, wind]])
    
    return jsonify({"prediction": prediction[0]})


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [outlook, setOutlook] = useState("sunny");
  const [temperature, setTemperature] = useState("hot");
  const [humidity, setHumidity] = useState("high");
  const [wind, setWind] = useState("weak");
  const [prediction, setPrediction] = useState("");

  const handlePredict = async () => {
    var headers = {}
    try {
      const response = await axios.post('http://127.0.0.1:5000/data', {
        outlook,
        temperature,
        humidity,
        wind,
      },      {
          headers: {
            headers, // Set the content type
            // Other headers if needed (e.g., Authorization)
          },
        });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  return (
    <div className="App"  style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Play Decision</h1>
      <div className="form-group">
        <label>
          Outlook: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <select value={outlook} onChange={(e) => setOutlook(e.target.value)}>
            <option value="sunny">Sunny</option>
            <option value="overcast">Overcast</option>
            <option value="rain">Rain</option>
          </select>
        </label>
      </div>
      <div className="form-group">
        <label>
          Temperature: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <select value={temperature} onChange={(e) => setTemperature(e.target.value)}>
            <option value="hot">Hot</option>
            <option value="mild">Mild</option>
            <option value="cool">Cool</option>
          </select>
        </label>
      </div>
      <div className="form-group">
        <label>
          Humidity: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <select value={humidity} onChange={(e) => setHumidity(e.target.value)}>
            <option value="high">High</option>
            <option value="normal">Normal</option>
          </select>
        </label>
      </div>
      <div className="form-group">
        <label>
          Wind: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <select value={wind} onChange={(e) => setWind(e.target.value)}>
            <option value="weak">Weak</option>
            <option value="strong">Strong</option>
          </select>
        </label>
      </div>
      <div className="container">
        <button onClick={handlePredict} className="predict-button">Predict</button>
        {prediction && <p className="prediction-text">Can We Play: {prediction}</p>}  
      </div>

    </div>
  );
}

export default App;



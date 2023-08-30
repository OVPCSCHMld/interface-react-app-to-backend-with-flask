import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = {
    "Day": ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14"],
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"],
    "Play Golf": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Map categorical features to numerical values
outlook_map = {"Sunny": 0, "Overcast": 1, "Rain": 2}
temperature_map = {"Hot": 0, "Mild": 1, "Cool": 2}
humidity_map = {"High": 0, "Normal": 1}
wind_map = {"Weak": 0, "Strong": 1}

df["Outlook"] = df["Outlook"].map(outlook_map)
df["Temperature"] = df["Temperature"].map(temperature_map)
df["Humidity"] = df["Humidity"].map(humidity_map)
df["Wind"] = df["Wind"].map(wind_map)

# Split the data into training and testing sets
X = df.drop(["Day", "Play Golf"], axis=1)  # Features
y = df["Play Golf"]  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[2]:


model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


# In[3]:


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")


# In[4]:


# Save the model to a file
joblib.dump(model, "decision_tree_model.pkl")



from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd

# Load the dataset
data = pd.read_csv("data/dados_codificados.csv")

# Create a linear regression model
model = LinearRegression()
X = data[["Age", "Annual Income (k$)", "Gender"]]
y = data["Spending Score (1-100)"]
model.fit(X, y)

# Scale the predicted values to the range [0, 100]
scaler = MinMaxScaler(feature_range=(0, 100))
y_pred_scaled = scaler.fit_transform(model.predict(X).reshape(-1, 1))

# Save the trained model and the scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

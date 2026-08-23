from sklearn.linear_model import LinearRegression
import joblib

model = LinearRegression()
model.fit([[1], [2], [3], [4], [5]], [2, 4, 6, 8, 10])

joblib.dump(model, "model/model.joblib")

print("Model saved successfully!")
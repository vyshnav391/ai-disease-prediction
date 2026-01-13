from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model (example: Random Forest)
model = pickle.load(open("models/random_forest.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])
    prediction = model.predict(final_features)

    result = "High Risk" if prediction[0] == 1 else "Low Risk"
    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)

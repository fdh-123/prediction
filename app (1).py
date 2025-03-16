from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("grid_search_modela.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html", prediction_text="")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form input
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features)[0]

        # Convert result to readable text
        result_text = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"

        # Send back the prediction to index.html
        return render_template("index.html", prediction_text=result_text)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)

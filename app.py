from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
with open("models/cv.pkl", "rb") as f:
    cv = pickle.load(f)
with open("models/clf.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route("/")
def home():
    return render_template("spam_classifier.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get('content')
    tokenized_email = cv.transform([email]) # X 
    prediction = clf.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    return render_template("spam_classifier.html", prediction=prediction, email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
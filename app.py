import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import statsmodels.api as sm

app = Flask(__name__)
model = joblib.load('HFD_model_1.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        output = "Negative"
    else:
        output = "Positive"

    return render_template("index.html", prediction_text='Heart Failure Diagnosis is {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

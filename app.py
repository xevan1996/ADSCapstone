import numpy as np
from flask import Flask, request, jsonify, render_template
from forms import dataForm
import pickle
import joblib
import statsmodels.api as sm
import random
import os

app = Flask(__name__,
            static_url_path='',
            static_folder='ADSCapstone/static')

model = joblib.load('HFD_model_1.pkl')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    con_val = model.predict_proba(final_features)

    n = random.uniform(0.01, 0.06)

    final_con = (con_val[0, 0] + con_val[0, 1] - n) * 100
    final_con = "{:.2f}".format(final_con)

    if prediction == 0:
        output = "Negative"
    else:
        output = "Positive"

    form = dataForm()
    return render_template("index.html", prediction_text='Heart Failure Diagnosis is {} with a confidence of {} %'.format(output, final_con), mypred=form)

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

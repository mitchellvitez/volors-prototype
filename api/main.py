import json
from flask import Flask, render_template, request, jsonify
import os
import base64
import sklearn
from sklearn.externals import joblib 
import glob
from classify import classify

app = Flask(__name__)

@app.route('/learn', methods=['POST'])
def learn():
    """Clean up data, train model, and dump to file. Return model name."""
    data = str(base64.b64decode(str(request.data)[str(request.data).find(',')+1:]))
    data = [row.split(',') for row in data.split('\\n')][:-1]
    model_name = data[0][-1]
    joblib.dump(classify(data[1:]), 'data/models/{}.pkl'.format(model_name))
    with open('data/headers/{}.json'.format(model_name), 'w') as outfile:
        json.dump(data[0], outfile)
    return jsonify(model_name)

@app.route('/headers/<model>')
def headers(model):
    """Return the list of data headers for a model."""
    with open('data/headers/{}.json'.format(model), 'r') as heads:
        return heads.read()

@app.route('/predict', methods=['POST'])
def predict():
    """Load the model and return a json-formatted prediction."""
    clf = joblib.load('data/{}.pkl'.format(request.form['model']))
    features = request.form['data'].split(',')
    prediction = clf.predict(features)
    return jsonify(prediction)

@app.route('/models', methods=['GET'])
def model_names():
    """Get list of model names for each model in the folder."""
    models = glob.glob('data/models/*.pkl')
    models = [os.path.splitext(os.path.basename(model))[0] for model in models]
    return jsonify(models)

if __name__ == "__main__":
    app.run(debug=True)

import json
from flask import Flask, render_template, request, jsonify
import os
import sklearn
from sklearn import neighbors
from sklearn.externals import joblib 
import numpy as np
import glob

app = Flask(__name__)

def classify(data):
    clf = neighbors.KNeighborsClassifier()
    data = np.array(data)
    # clf.fit(all but last column, last column)
    clf.fit(np.delete(data, -1, 1), data[:,-1])
    return clf

@app.route('/learn', methods=['POST'])
def train():
    f = str(request.files['data'].read())
    f = [row.split(',') for row in f.split('\\n')][:-1]
    model_name = f[0][-1]
    joblib.dump(classify(f[1:]), 'data/{}.pkl'.format(model_name))
    return jsonify(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    clf = joblib.load('data/{}.pkl'.format(request.form['model']))
    features = request.form['data'].split(',')
    prediction = clf.predict(features)[0]
    return jsonify(prediction)

@app.route('/models', methods=['GET'])
def model_names():
    models = glob.glob('data/*.pkl')
    models = [os.path.splitext(os.path.basename(model))[0] for model in models]
    return jsonify(models)

if __name__ == "__main__":
    app.run(debug=True)

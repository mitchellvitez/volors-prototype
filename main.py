from flask import Flask, render_template, request
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

@app.route('/learn', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        f = str(request.files['data'].read())
        f = [row.split(',') for row in f.split('\\n')][:-1]
        model_name = f[0][-1]
        joblib.dump(classify(f[1:]), 'data/{}.pkl'.format(model_name))
        return render_template('trained.html', model_name=model_name)

    return render_template('upload_csv.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        clf = joblib.load('data/{}.pkl'.format(request.form['model']))
        features = request.form['data'].split(',')
        prediction = clf.predict(features)[0]
        return render_template('prediction.html', prediction=prediction)

    models = glob.glob('data/*.pkl')
    models = [os.path.splitext(os.path.basename(model))[0] for model in models]
    return render_template('predict.html', models=models)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

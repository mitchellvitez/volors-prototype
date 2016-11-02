from flask import Flask, render_template, request

import sklearn
from sklearn import tree
from sklearn.externals import joblib 
import numpy as np
import glob

app = Flask(__name__)

def classify(f):
    clf = tree.DecisionTreeClassifier()
    f = np.array(f)
    clf.fit(np.delete(f, -1, 1), f[:,-1])
    return clf

@app.route('/learn', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        f = str(request.files['data'].read())
        f = [row.split(',') for row in f.split('\\n')][:-1]
        joblib.dump(classify(f[1:]), '{}.pkl'.format(f[0][-1]))
        return "Trained to classify by {} and saved model to {}.pkl. Visit /predict to use this model.".format(f[0][-1], f[0][-1])

    return render_template('upload_csv.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        clf = joblib.load('{}'.format(request.form['model']))
        d = request.form['data'].split(',')
        prediction = clf.predict(d)[0]
        return "We predict class {}".format(prediction)

    return render_template('predict.html', models=glob.glob('*.pkl'))

if __name__ == "__main__":
    app.run()

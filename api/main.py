import json
from flask import Flask, render_template, request, jsonify
import os
import base64
import sklearn
from sklearn.externals import joblib 
import glob
from classify import classify

app = Flask('Volors')

@app.route('/learn', methods=['POST'])
def learn():
    """Clean up data, train model, and dump to file. Return model name.

    Takes a base64-encoded csv file
    Returns model name as string
    """
    data = str(base64.b64decode(str(request.data)[str(request.data).find(',')+1:]))
    data = [row.split(',') for row in data.split('\\n')][:-1]
    model_name = data[0][-1]
    joblib.dump(classify(data[1:]), 'data/models/{}.pkl'.format(model_name))
    with open('data/headers/{}.json'.format(model_name), 'w') as outfile:
        json.dump(data[0], outfile)
    return jsonify(model_name)

@app.route('/headers/<model_name>')
def headers(model_name):
    """Return the list of data headers for a model
    
    Takes a model name as string
    Returns json list of header names as strings
    """
    with open('data/headers/{}.json'.format(model_name), 'r') as heads:
        return heads.read()

@app.route('/predict', methods=['POST'])
def predict():
    """Load the model and return a json-formatted prediction
    
    Takes a form with 'model' attribute set to model name
    Returns the prediction array for csv features ('data')
    """
    clf = joblib.load('data/{}.pkl'.format(request.form['model']))
    features = request.form['data'].split(',')
    prediction = clf.predict(features)
    return jsonify(prediction)

@app.route('/models', methods=['GET'])
def model_names():
    """Get list of model names for each model in the folder
    
    Returns json list of model names as strings.
    """
    models = glob.glob('data/models/*.pkl')
    models = [os.path.splitext(os.path.basename(model))[0] for model in models]
    return jsonify(models)

def routes_markdown():
    with open('routes.md', 'w+') as f:
        f.write('# {} Routes\n\n'.format(app.name))

        for rule in sorted(app.url_map.iter_rules(), key=lambda x: x.endpoint):
            if rule.endpoint in ['static']:
                continue
            f.write('## {}\n\n'.format(str(rule).replace('<', '[').replace('>', ']')))

            for method in rule.methods:
                if method in ['OPTIONS', 'HEAD']:
                    continue
                f.write('`{}` '.format(method))
            f.write('\n\n')

            f.write(globals().get(rule.endpoint).__doc__ + '\n\n')

if __name__ == "__main__":
    routes_markdown()
    app.run(debug=True)

''' This module contains a knn classifier; it can build a model or use a model to make classifications

-The model is trained by accepting an array of data, the column names, and the column to classify
-The model is used to make classifications by accepting a data point to classify, the trained model, and the header
'''

import sys
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
import math

class KNN_classifier:
    '''This class builds and uses models for making knn classifications
    
    '''
    def __init__(self, training_data, column_names, column_to_predict):
        '''Initializes the class based on training data, names for available columns, and columns to predict

        the training data will build the model, the names will be handy for selecting which column to take
            we will later train a model to classify the selected column name
        '''

        self.training_data = training_data
        self.column_names = column_names
        self.to_predict = column_to_predict
        self.trained_clf = None
        self.metric = None

    def train_model(self):
        '''Trains a knn classifier based on training data to classify the column of interest based on the others

        Does some fairly wide-netted cross validation to select the best parameters, and then returns the model
        for use later and the scoring metric value that this model achieved
        NOTE: if there are column names given by the user, this function will still expect 
        that they are passed in here as integers or something else to denote the correct response var
        '''

        #figures out how many different sizes of neighbors to try in cross validation
        n_neighbors = [3,5]+range(6,int(math.log(len(self.training_data))),3)
        if len(self.training_data) < 5:
            n_neighbors = range(1,len(training_data))

        #sets cross validation params
        params = {"n_neighbors":n_neighbors, "weights":["uniform","distance"] }
        #creates the KNC classifier to cross-validate on
        knn = KNC()
        clf = GridSearchCV(knn, params)

        #get the idx of the header we're gonna predict or throw an exception if it's not found
        pred_col_idx = -1
        for idx in range(len(self.column_names)):
            if self.column_names[idx] == self.to_predict:
                pred_col_idx = idx
        if pred_col_idx == -1:
            raise ValueError("invalid column name for your dataset") 

        #remove response column from training data and place it in train_response
        train_features = np.delete(self.training_data, pred_col_idx, 1)
        train_response = self.training_data[:,pred_col_idx]
        #fit and return best model + it's scoring metric on the complete dataset
        clf.fit(train_features, train_response)
        self.trained_clf = clf.get_params()['estimator'].fit(train_features, train_response)
        self.metric = self.trained_clf.score(train_features, train_response)
        #return classifier with best CV params trained on the whole dataset and the metric of its success
        return self.trained_clf, self.metric

    def save_model(self):
        ''' Saves a copy of the model to disk in case we want to use it again later

        The format for the filename of the model is "knn_model_to_classify_"+<header name of response var>
        '''

        joblib.dump(self.trained_clf, "knn_model_to_classify_"+str(self.to_predict))
        return
    
    def load_model(self):
        ''' loads a copy of the model from disk in case when we want to use it

        The format for the filename of the model is "knn_model_to_classify_"+<header name of response var>
        '''

        clf = joblib.load("knn_model_to_classify_"+str(self.to_predict))
        return clf

def main():
    ''' This method contains some basic sanity checks to see if the knn_classifier crator above is working

    Uses the sklearn iris dataset to test whether the KNN_classifier class and its train_model wunction are
    completely broken
    '''

    from sklearn import datasets
    iris = datasets.load_iris()
    #add sklearn's response variable into the dataset like it would be in our layout
    added_response = np.array([ np.append(i,[j]) for i,j in zip(iris.data, iris.target)])
    #feed the iris dataset in as it would be if it were given by a user
    knn_clf = KNN_classifier(added_response, iris.feature_names+["response"], 'response')
    clf, score, = knn_clf.train_model()
    print clf
    print score

    knn_clf.save_model()
    recovered_clf = knn_clf.load_model()
    pred_col_idx = len(iris.feature_names)
    train_features = np.delete(added_response, pred_col_idx, 1)
    train_response = added_response[:,pred_col_idx]

    recovered_metric = recovered_clf.score(train_features, train_response)
    print recovered_clf
    print recovered_metric

if __name__ == "__main__":
    main()


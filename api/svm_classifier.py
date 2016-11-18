''' This module contains a svm classifier; it can build a model or use a model to make classifications

-The model is trained by accepting an array of data, the column names, and the column to classify
-The model is used to make classifications by accepting a data point to classify, the trained model, and the header
'''

import sys
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.externals import joblib
import math
import Classifier
from sklearn import datasets

class SVM_classifier(Classifier.Classifier):
    '''This class builds and uses models for making svm classifications
    
    '''

    def train_model(self):
        '''Trains a svm classifier based on training data to classify the column of interest based on the others

        Does some fairly wide-netted cross validation to select the best parameters, and then returns the model
        for use later and the scoring metric value that this model achieved
        NOTE: if there are column names given by the user, this function will still expect 
        that they are passed in here as integers or something else to denote the correct response var
        '''

        #creates ranges of C and Gamma parameters to grid search over
        #gamma determines how influential a single training example reaches
        #C parameter determines how weighted the model is towards simplicity; low C = less complex model
        C_range = np.logspace(-2,10,13)
        gamma_range = np.logspace(-9, 3,13)
        params = {'C': C_range, 'gamma':gamma_range}

        #creates the svc classifier to cross-validate on
        svm = SVC()
        clf = GridSearchCV(svm, param_grid=params)
        
        #gets the training feature vectors and response var vector
        train_features, train_response = self.get_train_features_and_response()
        
        #returns the trained model 
        return self.get_trained_model(clf, train_features, train_response)

def main():

    iris=datasets.load_iris()
    added_response = np.array([ np.append(i,[j]) for i,j in zip(iris.data, iris.target)])
    svm_clf = SVM_classifier(added_response, iris.feature_names+["response"], 'response')
    clf, score = svm_clf.train_model()
    print clf, score
    
    #this prefix would probably need to be much more descriptive in production
    svm_clf.save_model(name="svm")
    recovered_clf = svm_clf.load_model(name="svm")

    #this is NOT how this would be used; I'm just doing it this way to grab a test dataset
    train_features, train_response = svm_clf.get_train_features_and_response()

    recovered_metric = recovered_clf.score(train_features, train_response)
    print recovered_clf, recovered_metric

if __name__ == "__main__":
    main()

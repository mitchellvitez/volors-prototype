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
import Classifier

class KNN_classifier(Classifier.Classifier):
    '''This class builds and uses models for making knn classifications
    
    '''

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
        
        #gets the training feature vectors and response var vector
        train_features, train_response = self.get_train_features_and_response()
        
        #returns the trained model 
        return self.get_trained_model(clf, train_features, train_response)

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
    
    #this prefix would probably need to be much more descriptive in production
    knn_clf.save_model(name="knn")
    recovered_clf = knn_clf.load_model(name="knn")

    #this is NOT how this would be used; I'm just doing it this way to grab a test dataset
    train_features, train_response = knn_clf.get_train_features_and_response()

    recovered_metric = recovered_clf.score(train_features, train_response)
    print recovered_clf
    print recovered_metric

if __name__ == "__main__":
    main()


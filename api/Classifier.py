import numpy as np
from sklearn.externals import joblib

class Classifier:
    '''A generic classifier class to define methods that other classifiers will need or use

    init -- initializes the class based on training data, names for columns, and col to predict
    train_model -- trains a classifier based on training data
    save_model -- saves a copy of the model to the filesystem in case we need it later
    load_model -- loads a copy of the model we created before when if want to use it
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

    def save_model(self, name="generic"):
        ''' Saves a copy of the model to disk in case we want to use it again later

        The format for the filename of the model is "knn_model_to_classify_"+<header name of response var>
        '''

        joblib.dump(self.trained_clf, name+"_model_to_classify_"+str(self.to_predict))
        return
    
    def load_model(self, name="generic"):
        ''' loads a copy of the model from disk in case when we want to use it

        The format for the filename of the model is "knn_model_to_classify_"+<header name of response var>
        '''

        clf = joblib.load(name+"_model_to_classify_"+str(self.to_predict))
        return clf

    def get_train_features_and_response(self):
        ''' given the training data separates the response col into a separate variable

        removes the column with the header selected to predict from the training feature vectors
        places it into its own numpy array so that it can be used to train the clf
        '''

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

        return train_features, train_response

    def get_trained_model(self, clf, train_features, train_response):
        ''' accepts a clf object with the parameter grid search and returns the best trained model

        accepts a clf with the gridsearch params already initialized along with train x and y data
        returns a model with the selected parameters trained on the entire dataset
        '''

        #fit and return best model + it's scoring metric on the complete dataset
        clf.fit(train_features, train_response)
        self.trained_clf = clf.get_params()['estimator'].fit(train_features, train_response)
        self.metric = self.trained_clf.score(train_features, train_response)
        #return classifier with best CV params trained on the whole dataset and the metric of its success
        return self.trained_clf, self.metric



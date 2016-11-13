#!/usr/bin/env python3
import unittest
import numpy as np
import get_data
import knn_classifier as knn_c
from sklearn import datasets

class TestTestingFramework(unittest.TestCase):
    def test_math(self):
        self.assertEqual(1, 1)

    def test_english(self):
        self.assertEqual('word', 'word')

    def test_get_data(self):
        types_test_file = "test/test_data/types_test.csv"
        missing_data_test_file = "test/test_data/missing_data_test.csv"
        types_test_data = get_data.get_data_from_file(types_test_file, test_mode=True)[1]
        missing_test_data = get_data.get_data_from_file(missing_data_test_file, test_mode=True)[1]
        self.assertEqual(4, len(types_test_data))
        self.assertEqual(3, len(types_test_data[0]))
        self.assertEqual("1.1", types_test_data[-1][-1])
        self.assertEqual(4, len(missing_test_data))
        self.assertEqual(3, len(missing_test_data[0]))
        
    def test_knn_classifier_runs(self):
        iris=datasets.load_iris()
        added_response = np.array([ np.append(i,[j]) for i,j in zip(iris.data, iris.target)])
        knn_clf = knn_c.KNN_classifier(added_response, iris.feature_names+["response"], 'response')
        clf, score = knn_clf.train_model()
        self.assertGreater(score, .9)
        self.assertEqual(5, clf.get_params()["n_neighbors"])
        

if __name__ == '__main__':
    unittest.main()

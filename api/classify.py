from sklearn import neighbors
import numpy as np

def classify(data):
    """Only does KNN classification for now."""
    clf = neighbors.KNeighborsClassifier()
    data = np.array(data)
    # clf.fit(all but last column, last column)
    clf.fit(np.delete(data, -1, 1), data[:,-1])
    return clf


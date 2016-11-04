import pandas as pd
import numpy as np
import werkzeug as wz
import math

'''
params: a working filename for a csv in this directory 
modifies: nothing
returns: the data from the csv as a numpy array
notes:
    uses pandas' default header inference
'''
def get_data_from_file(f_name):
    #create a safe filename
    safe_f = wz.secure_filename(f_name)
    #pandas will infer headers or not by default, I'm willing to trust them to do a better job than I
    data_frame = pd.read_csv(safe_f)
    #we're only gonna want the data as a numpy array, not the headers
    return list(data_frame.columns), data_frame.values

'''
params: data, a numpy array as would be returned by get_data_from_file
modifies nothing
returns: 
    True if the data has > 0 rows, all rows have same # of features
    False if the input data fails to meet any of the above criteria
NOTE:
    I don't think pandas will allow different types to be in the same column unless one of them is an nan
'''
def check_data_usability(data):
    #makes sure there is at least one row
    if len(data) <= 0:
        return False
    #makes sure each row has the same dimensions
    all_dimensions_match = all([row.shape == data[0].shape for row in data])
    if not all_dimensions_match:
        return False
    #both criteria were met
    return True

def main():
    sample_test_file = "sample.csv"
    types_test_file = "types_test.csv"
    missing_data_test_file = "missing_data_test.csv"
    files = [sample_test_file, types_test_file, missing_data_test_file]
    for f in files:
        print get_data_from_file(f)[1]
        print check_data_usability(get_data_from_file(f)[1])
        print ""

if __name__ == "__main__" :
    main()

''' this module, get_data.py, is a module for handling data input

This module contains the functions get_data_from_file and is_usable
-get_data_from_file is intended to safely read a csv and then return the headers and data it contains
-is_usable checks whether the data should be safe to use with sklearn
'''

import pandas as pd
import numpy as np
import werkzeug as wz

def get_data_from_file(f_name):
    '''This function collects data from a csv and returns the headers and data

    argument: a working filename for a csv in this directory 
    modifies: nothing
    returns: the headers of the csv as a list, and the data contained in the csv as an ndarray
    notes:
        uses pandas' default header inference to determine what are headers
    '''

    #create a safe filename
    safe_f = wz.secure_filename(f_name)
    #pandas will infer headers or not by default, I'm willing to trust them to do a better job than I
    data_frame = pd.read_csv(safe_f)
    #we're only gonna want the data as a numpy array, not the headers
    return list(data_frame.columns), data_frame.values

def is_usable(data):
    ''' a function to determine whether or not the data is well-formed enough for use

    argument: data, a numpy array as would be returned by get_data_from_file
    modifies nothing
    returns: 
        True if the data has > 0 rows, all rows have same # of features
        False if the input data fails to meet any of the above criteria
    NOTE:
        I don't think pandas will allow different types to be in the same column unless one of them is an nan
        which all become floats for some reason
    '''

    #makes sure there is at least one row
    if len(data) <= 0:
        return False
    #makes sure each row has the same dimensions
    all_dimensions_match = all([row.shape == data[0].shape for row in data])
    if not all_dimensions_match:
        return False
    #both criteria were met
    return True


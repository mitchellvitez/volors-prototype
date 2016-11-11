''' This file contains tests for the functions defined in get_data
 
Contains one function, main, which runs some simple tests on get_data's functions, get_data_from_file and is_usable
'''

import sys
sys.path.append("../data")
import get_data

def main():
    ''' Runs simple tests on get_data_from_file and is_usable functions of get_data module in data dir

    args: none
    modifies: IO
    requires: that the types_test.csv and missing_data_test.csv files are in this dir
    returns: non
    '''
    types_test_file = "types_test.csv"
    missing_data_test_file = "missing_data_test.csv"
    files = [types_test_file, missing_data_test_file]
    for f in files:
        print(get_data.get_data_from_file(f)[1])
        print(get_data.is_usable(get_data.get_data_from_file(f)[1]))
        print("")

if __name__ == "__main__" :
    main()

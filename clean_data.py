#importing needed libraries 

import pandas as pd 
import numpy as np 
import argparse 
import load_data from dirty-data 


def clean_missing_val(df): 
    df.dropna()
    return df  

if __name__ == '__main__':
    # Parse command-line arguments (fall back to defaults)
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", default=DEFAULT_INPUT_FILE, help="Path to the input CSV file")
    args = parser.parse_args()
    
    messy_file = load_data(args.input_csv)

    clean_missing_val(messy_file)
    






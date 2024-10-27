#importing needed libraries 

import pandas as pd 
import numpy as np 
import argparse 


def load_data(file_path):
    df = pd.read_csv(file_path)
    df = pd.DataFrame(df)
    return df

def clean_missing_val(df): 
    df = df.dropna()
    return df  

def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df 

def outliers(df): 
    df = df[df['year'] <= 2023]
    df = df[df['population'] < 1000000000]
    df = df[df['gender'] < 3]
    df['income_groups'] = df['income_groups'].str.replace('_typo', '', regex=False)
    return df 

def data_type(df): 
    df['gender'] = df['gender'].astype('object')
    return df 

if __name__ == '__main__':

    #defining command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to save the output CSV file")
    args = parser.parse_args()
    
    #applying functions to messy dataset 
    messy_file = load_data(args.input_csv)
    messy_file = clean_missing_val(messy_file)
    messy_file = remove_duplicates(messy_file)
    messy_file = outliers(messy_file)
    messy_file = data_type(messy_file)
    
    #saving clean dataset 
    messy_file.to_csv(args.output_file, index=False)
    print(f"\nMessy dataset saved as '{args.output_file}'")


    






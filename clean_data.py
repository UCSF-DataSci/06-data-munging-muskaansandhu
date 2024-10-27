#importing needed libraries 

import pandas as pd 
import numpy as np 
import argparse 

#loading in the messy dataset and returing it as a pandas dataframe 
def load_data(file_path):
    df = pd.read_csv(file_path)
    df = pd.DataFrame(df)
    return df

#function that will take the dataframe as input and drop all missing values 
def clean_missing_val(df): 
    df = df.dropna()
    return df  

#function that will take dataframe as input and drop all duplicated rows, keeping the first instance of any duplicated row 
def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df 

#function that filters rows up to 2023, removes outliers from the population column by calculating the IQR and 1st and 3rd quantiles, filters rows for gender to only contain 1 and 2, and replaces '_typo' values in income_groups column
def outliers(df): 
    df = df[df['year'] <= 2023]
    quantile_1 = df['population'].quantile(0.25)
    quantile_3 = df['population'].quantile(0.75)
    range = quantile_3 - quantile_1 
    df = df[(df['population'] > (quantile_1 - 1.5 * range)) & (df['population'] < (quantile_3 + 1.5 * range))]
    df = df[df['gender'] < 3]
    df['income_groups'] = df['income_groups'].str.replace('_typo', '', regex=False)
    return df 

#changing gender into a categorical variable by changing the type to object 
def data_type(df): 
    df['gender'] = df['gender'].astype('object')
    return df 

if __name__ == '__main__':

    #defining command line arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to save the output CSV file")
    args = parser.parse_args()
    
    try: 
    #applying functions to messy dataset 
        messy_file = load_data(args.input_csv)
        messy_file = clean_missing_val(messy_file)
        messy_file = remove_duplicates(messy_file)
        messy_file = outliers(messy_file)
        messy_file = data_type(messy_file)
        
    
    #saving clean dataset 
        messy_file.to_csv(args.output_file, index=False)
        print(f"\nMessy dataset saved as '{args.output_file}'")
    except Exception as e: #error handling that highlights potential issues while running the script 
        print(f"Error: An issue occurred while running the script - {e}")


    






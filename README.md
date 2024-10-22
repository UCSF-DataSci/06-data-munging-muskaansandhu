# PART 1: EXPLORATORY DATA ANALYSIS** 

*DATASET OVERVIEW*
- Name: messy_population_data.csv
- Rows: 125718
- Columns: 5

*ISSUES PRESENT* 

## 1) Missing values

In order to determine the missing values from the dataset, I ran the following: 
`dt.isnull().sum()` 
,which gave me the following output: 

|   Variable  | Missing |
|-------------|---------|
|income_groups| 6306    |
|    age      | 6223    |
|   gender    | 5907    |
|    year     | 6202    |
|  population | 6340    |

There are missing values within all five columns of the dataset. If left uncleaned, the missing values present a huge loss of information. 

## 2) Duplicated values 

To identify duplicated values, I ran `dt.duplicated.sum()`, which gave me a total of *2950* rows which were duplicated. I filtered through the duplicated rows by running
``` 
dt_duplicated = dt.duplicated()
dt[dt_duplicated]
```

## 3) Outliers 

To look at potential outliers from the dataset, I ran ``. 

## 4) 

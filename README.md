# PART 1: EXPLORATORY DATA ANALYSIS** 

*DATASET OVERVIEW* 
- Name: messy_population_data.csv
- Rows: 125718
- Columns: 5

*ISSUES PRESENT* 

**1) Missing values**

In order to determine the missing values from the dataset, I ran the following: 
`dt.isnull().sum()` 
Which gave me the following output: 

|   Variable  | Missing |
|-------------|---------|
|income_groups| 6306    |
|    age      | 6223    |
|   gender    | 5907    |
|    year     | 6202    |
|  population | 6340    |

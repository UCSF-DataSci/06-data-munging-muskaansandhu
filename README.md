# PART 1: EXPLORATORY DATA ANALYSIS

### *DATASET OVERVIEW*
- Name: messy_population_data.csv
- Rows: 125718
- Columns: 5

### *ISSUES PRESENT* 

As a note, the following contains snippets of code I used to evalute the messy dataset. In the repo, there is a Jupyter notebook that is titled "eda_analysis.ipynb" which contains all the code and associated outputs! 

#### 1) Missing values

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

There are missing values within all five columns of the dataset. If left uncleaned, the missing values present a huge loss of information and will affect the types of statistical analyses we can conduct and how to interpret those results. 

#### 2) Duplicated values 

To identify duplicated values, I ran `dt.duplicated.sum()`, which gave me a total of *2950* rows which were duplicated. I filtered through the duplicated rows by running
``` 
dt_duplicated = dt.duplicated()
dt[dt_duplicated]
```
Duplicated values, like missing values, will lead to difficulty interpreting and conducting any type of analyses with your data. Duplicated data gives you biased representation of your sample. 

#### 3) Outliers 

To look at potential outliers from the dataset, I used the `describe()` function on the numeric variables. These are the results I got: 

|   Variable  |   mean       | sd           | min | 25%        | 50%        | 75%        | max           | 
|-------------|--------------|--------------|-----|------------|------------|------------|---------------|
|population   | 111298303.15 |1265205486.84 | 21  | 2316023.00 | 7145753.50 |14663884.50 |32930428000.00 |
|    age      | 50.1         | 29.15        | 0   | 25         | 50         |75          | 100           |
|    year     | 2025.07      | 43.58        |1950 | 1987       | 2025       | 2063       |  2119         |

Based on this, it seems that the population and year column was affected by the addition of outliers. The maximum values for both of those columnn, and the minimum value for population, indicate that there are inplausible values present. These outliers can skew our perception of the underlying distribution of the data, and in turn, lead to biased results for any analyses conducted. 

When looking at the two categorical variables in the dataset, I examined their unique values to see if there were anything that didn't make any sense. Using the code  `print(dt['income_groups'].unique())`, I found that there in addition to the missing values we know the column has, there are occurences with the suffix "_typo". In addition, when looking at gender, `print(dt['gender'].unique())`, shows that there is an additional category marked "3". These extra categories add unecessary complexity to the dataset and can make it difficult determine how many true instances there are for a given category. It is important to keep conscise names for all values in a categorical variable for ease of interpretation. 

#### 4) Inconsistent data types 

To check the type of data each column in the dataframe, I used `dt.dtypes`. This told me that all the columns were numeric, except for the income group category. Since gender here is categorical, it is important to define it as such. Making sure that your variables are categorized correctly is critical because gender as a continuous variable does not make any sense and will not be interpreted correctly as such. 

# PART 2: CLEANING THE DATA 


# PART 3: DOCUMENTING RESULTS

### *DATASET OVERVIEW*
- Name: cleaned_population_data.csv
- Rows: 125718
- Columns: 5

#### 1) Description of cleaned dataset 

#### 2) Challenges faced 

#### 3) Reflection + room for improvement 

Having the `dirt-data.py` file to refer back to in order to determine how the data set was transformed to become "messy" was very convienent in order to complete this assignment. Unfortunately, this will not be the case in real life. I think 





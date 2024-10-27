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

#### 1) Missing values
To handle this issue, I removed all the rows which contained missing values using the `dropna()` function. Since we don't have much information about the original dataset, it would be hard to determine which other missing data techiques make sense to use in this scenario, such as imputation.  

#### 2) Duplicated values 
The easiest way to remove duplicated values is to use `drop_duplicates()` function. I made the assumption that the first duplicated row in the dataframe was the one to keep. 

#### 3) Outliers 
To deal with outliers involved the year, I filtered for rows that had data up to 2023. I had assumed that the dataset we were given only had complete data up till the most recent year, 2023. To deal with outliers involving population, I calculated the interquartile range. The interquartile range describes the spread of data from the 25th percentile to the 75th percentile. A data point is considered an outlier if it is less than the 25th percentile + 1.5 x interquartile range or greater than the 75th percentile + 1.5 x interquartile range. I filtered for these rows as such. I also filtered for rows that had the value of "3" for gender, since this was an ambiguous value introduced in the dataset. For the values in the income group column which included "_typo", I removed them so the unqiue values of the column would be strictly limited to high, low, lower middle, and upper middle income. 

After filtering for outliers, duplicated values, and missing values, the dataset reduced from 125718 to 39901 rows. The dataset was roughly reduced by triple. 

#### 4) Inconsistent data types 
Finally, I changed the data type of the gender column to object, which made sure that it was treated as a categorical variable instead of a numerical variable. 

# PART 3: DOCUMENTING RESULTS

### *DATASET OVERVIEW*
- Name: cleaned_population_data.csv
- Rows: 39901
- Columns: 5

#### 1) Description of cleaned dataset 
|   Variable  |   mean       | sd           | min | 25%        | 50%        | 75%        | max           | 
|-------------|--------------|--------------|-----|------------|------------|------------|---------------|
|population   | 4799508.60   |4878418.41    | 22  | 656379.00  | 3556219.00 |7379419.00  |19628109.00    |
|    age      | 53.01        | 28.45        | 0   | 30         | 54         |77          | 100           |
|    year     | 1985.24      | 21.34        |1950 | 1967       | 1985       | 2004       |  2023         |

#### 2) Challenges faced 
The main challenge with this assingment was how to deal with the outliers. Since I didn't have any underlying information about the dataset an where it came from, I couldn't properly filter for the year and population values that were implausible. If I knew the range of years in which data was collected and the countrys from where population was recorded, I could do additional research to determine accurate population sizes and keep the original years in the dataset. Hence, calculating outliers by using the interquartile range and assuming thatI had data from up till 2023 was the best possible option I could think of for data cleaning. Additionaly, removing rows with missing and duplicated values significantly reduced the size of data set. If I knew more about the data, I could have tried imputing some values by using the mean values but that seemed impractical in this situation given that the data was messy to begin with and I had no other information to go off of. 

#### 3) Reflection + room for improvement 

Having the `dirt-data.py` file to refer back to in order to determine how the data set was transformed to become "messy" was very convienent in order to complete this assignment. Unfortunately, this will not be the case in real life. I think this activty showed how important exploratory data analysis is for finding issues in your dataset. Additionaly, this exercise emphasized the importance of knowing where your data comes from. Having information as to how the data was sources and some type of codebook is essential to making critical decsions in the data cleaning process. In terms of improvement, I can definentely find more ways to limit the amount of data I remove since my final data set is a third of what I started with. We want to have as much data as possible prior to starting analysis, the more information the better! 





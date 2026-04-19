import pandas as pd

def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented in this dataset? 
    # This will return a Pandas Series with race names as the index.
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    # We filter for 'Male', select the 'age' column, and calculate the mean.
    # We use .round(1) to keep the output clean.
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men
    }
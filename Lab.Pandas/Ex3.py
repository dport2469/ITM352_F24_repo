# Create a dataframe from individual lists.  Do some simple statistics on that dataframe.
import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]

#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Create a list of age gender tuples from these lists
age_gender = list(zip(ages, gender))

# Convert the list of tuples to a DataFrame, with names as the index
df = pd.DataFrame(age_gender, columns=['Age', 'Gender'], index=names)

# Summarize the DataFrame using the describe method
print(df)
summary = df.describe()
print(summary)

# Calculate the average age by gender
average_age_by_gender = df.groupby('Gender')['Age'].mean()
print(average_age_by_gender)

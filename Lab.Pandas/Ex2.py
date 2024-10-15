import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Create a DataFrame
data = {
    'Name': names,
    'Age': ages,
    'Gender': gender
}
df = pd.DataFrame(data)

# Calculate average age by gender
average_age_by_gender = df.groupby('Gender')['Age'].mean()

print(average_age_by_gender)
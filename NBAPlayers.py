import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your dataset is a CSV file, adjust the path and format accordingly
dataset = pd.read_csv("C:/Users/mahlo/OneDrive/Documents/NBAPlayers/NBA-playerlist.csv")

# Assuming 'dataset' is your loaded DataFrame

# Display basic statistics of numerical columns
numerical_summary = dataset.describe()
print("Numerical Summary:\n", numerical_summary)

# Display distribution of categorical columns
categorical_columns = dataset.select_dtypes(include='object').columns
for column in categorical_columns:
    print(f"\nDistribution of {column}:")
    print(dataset[column].value_counts())

# Identify relevant numerical columns for correlation analysis
numerical_columns_for_correlation = dataset.select_dtypes(include=['int64']).columns

# Visualize the correlation between numerical features
correlation_matrix = dataset[numerical_columns_for_correlation].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Visualize the distribution of numerical features
plt.figure(figsize=(15, 10))
dataset.boxplot(rot=45)
plt.title("Distribution of Numerical Features")
plt.show()

# Visualize the distribution of selected categorical features
selected_categorical_columns = ['TEAM_ABBREVIATION', 'TEAM_CITY']
for column in selected_categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=dataset, x=column)
    plt.title(f"Distribution of {column}")
    plt.show()

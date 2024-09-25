# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load your NBA dataset
file_path = 'C:/Users/mahlo/OneDrive/Documents/NBAPlayers/NBA-playerlist.csv'
nba_data = pd.read_csv(file_path)

# Print a message to indicate the script is running
print("Running Career Length Predictor script...")

# EDA and Data Cleanup
# For EDA, let's visualize the relationship between 'FROM_YEAR' and 'TO_YEAR'
sns.scatterplot(x='FROM_YEAR', y='TO_YEAR', data=nba_data)
plt.title('Relationship between FROM_YEAR and TO_YEAR')
plt.show()

# Handle missing values
threshold = 0.1 * len(nba_data)
nba_data = nba_data.dropna(axis=1, thresh=threshold)

# Remove unnecessary columns
columns_to_remove = ['DISPLAY_LAST_COMMA_FIRST', 'PLAYERCODE']
nba_data = nba_data.drop(columns=columns_to_remove)

# Feature selection - Placeholder features, replace with actual features
features = ['FROM_YEAR', 'OTHERLEAGUE_EXPERIENCE_CH']
target = 'TO_YEAR'  # Replace with the actual column name

# Extract features and target variable
X = nba_data[features]
y = nba_data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Print a message to indicate the completion of the script
print("Career Length Predictor script completed.")

# Print the evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Add additional print statements to check variables
print("Debugging: mse =", mse)
print("Debugging: r2 =", r2)

# Visualize the predicted vs. actual values
plt.scatter(y_test, predictions)
plt.xlabel('Actual Career End Year')
plt.ylabel('Predicted Career End Year')
plt.title('Actual vs. Predicted Career End Year')
plt.show()

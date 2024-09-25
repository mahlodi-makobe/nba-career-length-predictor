# Import necessary libraries
import pandas as pd

# Load your NBA dataset
file_path = 'C:/Users/mahlo/OneDrive/Documents/NBAPlayers/NBA-playerlist.csv'
nba_data = pd.read_csv(file_path)

# Handle missing values
# In this example, let's drop columns with more than 10% missing values
threshold = 0.1 * len(nba_data)
nba_data = nba_data.dropna(axis=1, thresh=threshold)

# Remove unnecessary columns
# In this example, let's remove 'DISPLAY_LAST_COMMA_FIRST' and 'PLAYERCODE' columns
columns_to_remove = ['DISPLAY_LAST_COMMA_FIRST', 'PLAYERCODE']
nba_data = nba_data.drop(columns=columns_to_remove)

# Display a summary of the cleaned dataset
cleaned_dataset_summary = nba_data.info()

# Print the summary
print(cleaned_dataset_summary)

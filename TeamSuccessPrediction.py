from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset
dataset = pd.read_csv("C:/Users/mahlo/OneDrive/Documents/NBAPlayers/NBA-playerlist.csv")

# Print unique values of 'ROSTERSTATUS' column
print(dataset['ROSTERSTATUS'].unique())
print(dataset['ROSTERSTATUS'].dtypes)

# Assuming 'Y' represents success and 'N' represents failure
if dataset['ROSTERSTATUS'].nunique() > 0:
    dataset['ROSTERSTATUS'] = dataset['ROSTERSTATUS'].map({'Y': 1, 'N': 0})
    target = 'ROSTERSTATUS'

    # Select relevant columns
    features = ['FROM_YEAR', 'GAMES_PLAYED_FLAG', 'OTHERLEAGUE_EXPERIENCE_CH', 'PERSON_ID', 'ROSTERSTATUS', 'TEAM_ID', 'TO_YEAR']

    # Filter relevant columns and remove rows with missing values
    data = dataset[features + [target]].dropna()

    # Check for missing values
    print(data.isnull().sum())

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42, shuffle=True)

    # Define the parameter grid to search
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [None, 10, 20],
        # Add more parameters to the grid if needed
    }

    # Create the Random Forest model
    rf_model = RandomForestRegressor(random_state=42)

    # Set up the GridSearchCV
    grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')

    # Fit the grid search to the data
    grid_search.fit(X_train, y_train)

    # Get the best parameters from the grid search
    best_params = grid_search.best_params_

    # Create and train the Random Forest model with the best parameters
    best_rf_model = RandomForestRegressor(random_state=42, **best_params)
    best_rf_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = best_rf_model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Best parameters: {best_params}')
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

else:
    print("No unique values found in 'ROSTERSTATUS' column. Unable to split data.")

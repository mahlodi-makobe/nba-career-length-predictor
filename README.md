# NBA Career Length Predictor

## Overview  
This project aims to predict the career length of NBA players based on historical data using various statistical models. It is a work-in-progress and serves as both a learning experiment and a practical application of data science techniques.

## Project Structure  
nba-career-length-predictor/  
│  
├── data/                     # Directory for datasets  
│   └── nba-playerlist.csv    # NBA dataset used for the prediction  
│  
├── notebooks/                # Jupyter notebooks for exploratory analysis (optional)  
│   └── exploratory_analysis.ipynb  
│  
├── src/                      # Source code directory  
│   └── career_length_predictor.py  # Main script for prediction  
│  
├── requirements.txt          # Dependencies required for the project  
│  
├── README.md                 # Project description and instructions  
│  
└── .gitignore                # Files to ignore (e.g., __pycache__/, .DS_Store)  

## Dataset  
The dataset used for this project contains information about NBA players, including their playing years and other attributes that may affect their career length. The data is stored in the `data/nba-playerlist.csv` file. 

**Columns:**  
- `FROM_YEAR`: The year the player started their NBA career.  
- `TO_YEAR`: The year the player ended their NBA career.  
- `OTHERLEAGUE_EXPERIENCE_CH`: Experience in other leagues.  
- Other columns include player attributes, but these need to be refined for the prediction model.

## Getting Started  

### Prerequisites  
- Python 3.7 or higher  
- The following Python libraries:  
  - pandas  
  - matplotlib  
  - seaborn  
  - scikit-learn  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/nba-career-length-predictor.git  
   cd nba-career-length-predictor

2.  Install the required packages:
   pip install -r requirements.txt  

3.  Place the nba-playerlist.csv file in the data/ directory.

  ###  Running the Script
1.  Navigate to the src/ directory
   cd src  
2.  Run the career_length_predictor.py script
   python career_length_predictor.py  
  This script will perform the following steps:
  - Load and preprocess the data.
  - Visualize key relationships in the dataset.
  - Train a linear regression model to predict the career length of NBA players.
  - Evaluate the model and print the results.

### Current Status
  - The current version is a basic implementation with placeholder features.
  - Ongoing improvements include refining the feature set, experimenting with different models and tuning the hyperparameters.

### Contributing
  Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

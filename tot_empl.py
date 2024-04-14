import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
from time import time

# Loaded variable 'df' from URI: /home/red/cda_project-1/data/2022_oes_ds_st_indus.csv


# Function to simulate missing values in a dataset
def simulate_missing(data, missing_percentage):
    data_copy = data.copy()
    missing_mask = np.random.rand(*data_copy.shape) < missing_percentage
    data_copy[missing_mask] = np.nan
    return data_copy


# Custom scorer function for evaluating model performance
def scorer(y_true, y_pred):
    if type(y_true) is pd.DataFrame:
        y_true = y_true.copy().values[:, -3:]
    else:
        y_true = y_true.copy()[:, -3:]

    if type(y_pred) is pd.DataFrame:
        y_pred = y_pred.copy().values[:, -3:]
    else:
        y_pred = y_pred.copy()[:, -3:]

    return mean_squared_error(y_true, y_pred)


# Function to prepare the data
def prep_data():
    """
    Reads a CSV file containing data on employment statistics and performs data preparation steps.

    Returns:
        pandas.DataFrame: The prepared DataFrame containing filtered and transformed data.
    """
    df = pd.read_csv(
        r"data/2022_oes_ds_st_indus.csv", na_values=["**", "*"], thousands=","
    )

    # Filter rows, data scientists at the state/industry level
    df = df[df["I_GROUP"].eq("sector") & df["O_GROUP"].eq("detailed")]

    # Drop columns except for state (AREA_TITLE), sector(NAICS_TITLE),
    # number of data scientists by state/sector (TOT_EMP),
    # % of state/sector that are data scientists (PCT_TOTAL)
    # Average data scientist salary by "State/Sector" (A_MEAN)
    df = df.drop(
        columns=[
            "AREA",
            "Unnamed: 0",
            "NAICS",
            "I_GROUP",
            "OCC_CODE",
            "OCC_TITLE",
            "O_GROUP",
            "EMP_PRSE",
            "MEAN_PRSE",
            "H_PCT10",
            "H_PCT25",
            "H_MEDIAN",
            "H_PCT75",
            "H_PCT90",
            "A_PCT10",
            "A_PCT25",
            "A_MEDIAN",
            "A_PCT75",
            "A_PCT90",
            "ANNUAL",
            "HOURLY",
            "H_MEAN",
        ]
    )

    return df


# Prepare the data
df = prep_data()

# For categorical features, build a list of categories
categories = [df["AREA_TITLE"].unique(), df["NAICS_TITLE"].unique()]

# Initialize the scaler, encoder, and imputer
scaler = StandardScaler()
encoder = OneHotEncoder(
    categories=categories,
    sparse_output=False,
)
imputer = IterativeImputer(BayesianRidge())

# Define the preprocessing steps using ColumnTransformer
preproc = ColumnTransformer(
    transformers=[
        ("cat", encoder, ["AREA_TITLE", "NAICS_TITLE"]),
        ("num", scaler, ["A_MEAN", "TOT_EMP", "PCT_TOTAL"]),
    ],
    n_jobs=-1,
)

# Create the model pipeline
model = Pipeline(steps=[("prep", preproc), ("impute", imputer)])

# Initialize KFold for cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize lists to store training and test errors
training_error = []
test_error = []
test_base_mean = []
test_base_median = []

# Copy the data for X and y
X = df.copy()
y = df.copy()

# Start the timer
start = time()

# Print setup time
print("Setup:", time() - start)

# Simulate missing values in selected columns
for col in ["A_MEAN", "TOT_EMP", "PCT_TOTAL"]:
    X[col] = simulate_missing(X[col].values, 0.05)

# Perform cross-validation
for i, (train_idx, test_idx) in enumerate(kf.split(df)):
    X_train = X.iloc[train_idx, :]
    X_test = X.iloc[test_idx, :]

    # Fit the model on the training data
    model.fit(X_train)

    # Transform the test data using the model
    y_test = model.transform(y.iloc[test_idx, :])
    y_pred = model.transform(X_test)

    # Create copies of X_test for mean and median imputation
    y_pred_mean = X_test.copy()
    y_pred_median = X_test.copy()

    # Perform mean and median imputation on missing values
    for col in X_test.select_dtypes("number"):
        mean = y_pred_mean[col].mean()
        median = y_pred_median[col].median()
        y_pred_mean[col] = y_pred_mean[col].fillna(value=mean)
        y_pred_median[col] = y_pred_median[col].fillna(value=median)

    # Print fold number and time taken
    print(f"Fold {i}: {time()-start:.2f} secs")

    # Calculate test errors
    test_error.append(
        mean_squared_error(
            y_test[:, -3:],
            y_pred[:, -3:],
        )
    )
    test_base_mean.append(
        mean_squared_error(
            y_test[:, -3:],
            y_pred_mean.iloc[:, -3:],
        )
    )
    test_base_median.append(
        mean_squared_error(
            y_test[:, -3:],
            y_pred_median.iloc[:, -3:],
        )
    )

# Print the mean of test errors, test_base_mean, and test_base_median
print(np.mean(test_error))
print(np.mean(test_base_mean))
print(np.mean(test_base_median))

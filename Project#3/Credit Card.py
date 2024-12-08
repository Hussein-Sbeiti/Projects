# %% [markdown]
# # Credit Card Fraud Detection and Analysis
# This notebook performs data preprocessing, classification, and clustering on a credit card fraud detection dataset.

# %%
# Import required libraries
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc, ConfusionMatrixDisplay
    

# %% [markdown]
# ## 1. Define Utility Functions
# Functions for searching files, handling data, and running models are defined below.

# %%

# Function to search for a CSV file by name
def find_csv_file(filename, start_dir="."):
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            file_path = os.path.join(root, filename)
            print(f"File found: {file_path}")
            return pd.read_csv(file_path)
    print(f"File '{filename}' not found.")
    return None

# Function to preprocess data
def preprocess_data(data, target_column):
    # Check if target column exists
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")

    # Drop rows where the target column has NaN
    print("Handling missing values in the target column...")
    data = data.dropna(subset=[target_column])

    # Separate features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Handle missing values in features
    print("Handling missing values in features...")
    X = X.fillna(X.median(numeric_only=True))  # Fill numeric NaN with median
    X = X.fillna("Missing")  # Fill categorical NaN with a placeholder value

    # Identify numeric and categorical columns
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns

    # Debugging: Print categorical columns before processing
    print(f"Categorical columns before processing: {categorical_cols}")

    # Handle categorical variables with high cardinality
    high_cardinality_cols = [col for col in categorical_cols if X[col].nunique() > 100]
    if high_cardinality_cols:
        print(f"Dropping high-cardinality columns: {high_cardinality_cols}")
        X = X.drop(columns=high_cardinality_cols)

    # Update the list of categorical columns after dropping high-cardinality ones
    categorical_cols = [col for col in categorical_cols if col not in high_cardinality_cols]

    # Apply one-hot encoding to remaining categorical variables
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

# %% [markdown]
# ## 2. Define Model Functions
# This section includes functions to train models and evaluate their performance.

# %%
# Function to train and evaluate a model
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{model_name} Report:")
    print(classification_report(y_test, y_pred))
    return model

# %% [markdown]
# ## 3. Main Workflow
# This section trains all the data 

# %%
def logistic_regression(X_train, X_test, y_train, y_test):
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Classification Report
    print("Logistic Regression Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap='Blues')
    plt.title("Logistic Regression - Confusion Matrix")
    plt.show()

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC curve (area = {roc_auc:.2f})")
    plt.plot([0, 1], [0, 1], 'k--')  # Random classifier line
    plt.title("Logistic Regression - ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.show()

    return model

# Decision Tree Classifier
def decision_tree_classifier(X_train, X_test, y_train, y_test):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Classification Report
    print("Decision Tree Classifier Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap='Purples')
    plt.title("Decision Tree - Confusion Matrix")
    plt.show()

    return model


# Random Forest Classifier
def random_forest(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Classification Report
    print("Random Forest Report:")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap='Greens')
    plt.title("Random Forest - Confusion Matrix")
    plt.show()

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC curve (area = {roc_auc:.2f})")
    plt.plot([0, 1], [0, 1], 'k--')  # Random classifier line
    plt.title("Random Forest - ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.show()

    return model



# K-Means Clustering
def kmeans_clustering(X, n_clusters=2):
    if X.shape[1] < 2:
        raise ValueError("Clustering requires at least two features.")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)

    # Visualizing the Clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.title(f'K-Means Clustering (n_clusters={n_clusters})')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

    return kmeans


# DBSCAN Clustering
def dbscan_clustering(X, eps=0.5, min_samples=5):
    if X.shape[1] < 2:
        raise ValueError("Clustering requires at least two features.")
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X)

    # Visualizing the Clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.title(f'DBSCAN Clustering (eps={eps}, min_samples={min_samples})')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

    return dbscan

# %% [markdown]
# ## 4. Main Workflow
# This section loads the dataset, preprocesses it, and runs the analysis.

# %%
def main():
    # File name of the merged dataset
    filename = 'Combined_data_3920.csv'
    
    try:
        # Search for the file on the desktop dynamically
        print("Searching for the merged dataset...")
        merged = find_csv_file(filename, start_dir=os.path.join(os.path.expanduser("~"), "Desktop"))
        if merged is None:
            print(f"File '{filename}' not found on the Desktop.")
            return
        print("Dataset loaded successfully.")
    except Exception as e:
        print(f"Failed to load the dataset: {e}")
        return

    # Define target column
    target_column = 'IsFraud'  # Update this to match your dataset's target column name
    
    if target_column not in merged.columns:
        print(f"Target column '{target_column}' not found in the dataset.")
        return

    # Preprocess data
    print("Preprocessing data...")
    try:
        X_train, X_test, y_train, y_test = preprocess_data(merged, target_column)
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return
    
    # Logistic Regression
    print("Running Logistic Regression...")
    logistic_model = logistic_regression(X_train, X_test, y_train, y_test)

    # Random Forest
    print("\nRunning Random Forest...")
    random_forest_model = random_forest(X_train, X_test, y_train, y_test)

    # Decision Tree Classifier
    print("\nRunning Decision Tree Classifier...")
    decision_tree_model = decision_tree_classifier(X_train, X_test, y_train, y_test)

    # Clustering
    print("\nScaling features for clustering...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    print("\nRunning K-Means Clustering...")
    clustering_features = X_train_scaled[:, :2]  # Use only the first two scaled features
    kmeans_model = kmeans_clustering(clustering_features)

    print("\nRunning DBSCAN Clustering...")
    dbscan_model = dbscan_clustering(clustering_features)

    print("\nAnalysis complete.")

main()

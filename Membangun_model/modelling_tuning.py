import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import mlflow
import dagshub
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = (
    PROJECT_ROOT
    / "Eksperimen_SML_BryanDhaniel"
    / "diabetes_prediction_preprocessing"
    / "diabetes_prediction_dataset_clean.csv"
)

def train_tuning_model():
    # Initialize DagsHub tracking (User must set environment variables or login)
    try:
        dagshub.init(repo_owner='BryanDhaniel', repo_name='Diabetes_Prediction', mlflow=True)
    except Exception as e:
        print("DagsHub not configured yet. Make sure to authenticate or replace USERNAME.")
        # fallback to local
        mlflow.set_tracking_uri("http://127.0.0.1:5000/")
        
    mlflow.set_experiment("Latihan_Diabetes_Prediction_Tuned")
    
    # Load dataset
    df = pd.read_csv(DATASET_PATH)
    df.dropna(inplace=True)
    
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mlflow.start_run(run_name="Tuned_RandomForest"):
        # Hyperparameter tuning
        param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10, 20]
        }
        
        rf = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)
        
        best_model = grid_search.best_estimator_
        
        # Logging parameters
        mlflow.log_params(grid_search.best_params_)
        
        # Evaluation
        y_pred = best_model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        # Logging metrics
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)
        mlflow.log_metric("f1_score", f1)
        
        # Logging model
        mlflow.sklearn.log_model(best_model, "model")
        
        # Save and log artifacts
        # 1. Metric Info JSON
        metrics_dict = {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1}
        with open("metric_info.json", "w") as f:
            json.dump(metrics_dict, f)
        mlflow.log_artifact("metric_info.json")
        
        # 2. Confusion Matrix Plot
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(6,5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig("training_confusion_matrix.png")
        mlflow.log_artifact("training_confusion_matrix.png")
        
        print(f"Tuning complete. Best params: {grid_search.best_params_}. Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_tuning_model()

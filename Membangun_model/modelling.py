import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow

# Auto logging
mlflow.autolog()

def train_model():
    # Set experiment
    mlflow.set_tracking_uri("http://127.0.0.1:5000/")
    mlflow.set_experiment("Latihan_Diabetes_Prediction")
    
    # Load dataset
    df = pd.read_csv('../Eksperimen_SML_BryanDhaniel/diabetes_prediction_preprocessing/diabetes_prediction_dataset_clean.csv')
    
    # Drop rows with NaN if any exist after cleaning
    df.dropna(inplace=True)
    
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Start MLflow run
    with mlflow.start_run(run_name="Basic_RandomForest"):
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        print(f"Model trained with accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_model()

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow

def train_model():
    mlflow.autolog()
    
    # Check if running in DagsHub action or locally
    df = pd.read_csv('diabetes_prediction_preprocessing/diabetes_prediction_dataset_clean.csv')
    df.dropna(inplace=True)
    
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mlflow.start_run():
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc:.4f}")

if __name__ == "__main__":
    train_model()

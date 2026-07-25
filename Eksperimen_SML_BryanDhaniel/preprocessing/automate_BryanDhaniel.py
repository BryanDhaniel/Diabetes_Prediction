import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

def preprocess_data(input_path, output_path):
    print(f"Loading data from {input_path}")
    df = pd.read_csv(input_path)
    
    print("Preprocessing data...")
    # Handle missing values
    df.dropna(inplace=True)
    
    # Encode categorical features
    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'])
    df['smoking_history'] = le.fit_transform(df['smoking_history'])
    
    # Save processed data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
    return df

if __name__ == "__main__":
    input_file = '../diabetes_prediction_raw/diabetes_prediction_dataset.csv'
    output_file = '../diabetes_prediction_preprocessing/diabetes_prediction_dataset_clean.csv'
    preprocess_data(input_file, output_file)

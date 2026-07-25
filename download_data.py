import urllib.request
import os

def download_data():
    print("Downloading dataset from HuggingFace...")
    url = "https://huggingface.co/datasets/marianeft/diabetes_prediction_dataset/resolve/main/diabetes_prediction_dataset.csv"
    output_path = 'Eksperimen_SML_BryanDhaniel/diabetes_prediction_raw/diabetes_prediction_dataset.csv'
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        urllib.request.urlretrieve(url, output_path)
        print(f"Download complete. Saved to {output_path}")
    except Exception as e:
        print(f"Failed to download csv. Trying to download parquet file... Error: {e}")
        url_parquet = "https://huggingface.co/datasets/marianeft/diabetes_prediction_dataset/resolve/main/data/train-00000-of-00001-c884cd92bd2e5192.parquet"
        output_parquet = 'Eksperimen_SML_BryanDhaniel/diabetes_prediction_raw/diabetes_prediction_dataset.parquet'
        urllib.request.urlretrieve(url_parquet, output_parquet)
        print(f"Download complete. Saved to {output_parquet}")

if __name__ == "__main__":
    download_data()

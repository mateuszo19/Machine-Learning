import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    data['feature1'] /= 10
    data['feature2'] /= 5
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw/sample_data.csv', 'data/processed/processed_data.csv')

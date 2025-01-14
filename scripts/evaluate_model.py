import pandas as pd
from sklearn.metrics import accuracy_score
import pickle


def evaluate_model(data_path, model_path):
    data = pd.read_csv(data_path)
    X = data[['feature1', 'feature2']]
    y = data['target']

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    predictions = model.predict(X)
    print(f"Accuracy: {accuracy_score(y, predictions):.2f}")


if __name__ == "__main__":
    evaluate_model('data/processed/processed_data.csv', 'models/model.pkl')

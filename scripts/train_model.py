import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


def train_model(data_path, model_path):
    data = pd.read_csv(data_path)
    X = data[['feature1', 'feature2']]
    y = data['target']

    model = LogisticRegression()
    model.fit(X, y)

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train_model('data/processed/processed_data.csv', 'models/model.pkl')

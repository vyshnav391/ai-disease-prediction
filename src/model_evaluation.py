from sklearn.metrics import accuracy_score, classification_report
import pickle
from data_preprocessing import preprocess_data

model = pickle.load(open("models/random_forest.pkl", "rb"))

X, y = preprocess_data("data/raw/dataset.csv")
predictions = model.predict(X)

print("Accuracy:", accuracy_score(y, predictions))
print(classification_report(y, predictions))

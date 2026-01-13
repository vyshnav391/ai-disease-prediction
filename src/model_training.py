from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from data_preprocessing import preprocess_data

X, y = preprocess_data("data/raw/dataset.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open("models/random_forest.pkl", "wb"))

print("Model trained and saved successfully")

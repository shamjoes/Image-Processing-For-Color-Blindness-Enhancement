import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.externals import joblib  # For saving the trained model

# Load your dataset
dataset_path = 'color_dataset.csv'
df = pd.read_csv(dataset_path)

# Features (X) and labels (y)
X = df[['R', 'G', 'B']]
y = df['color_label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Save the trained model for later use
model_filename = 'color_detection_model.pkl'
joblib.dump(rf_classifier, model_filename)

# Optionally, you can print a classification report for more detailed evaluation
print(classification_report(y_test, y_pred))

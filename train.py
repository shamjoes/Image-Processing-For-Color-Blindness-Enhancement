import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump  # Use joblib directly for saving and loading the model

# Load your dataset
dataset_path = 'colors.csv'
df = pd.read_csv(dataset_path)

# Print the first few rows of the DataFrame to inspect its structure
print(df.head())

# Print the column names in the DataFrame
print(df.columns)

# Features (X) and labels (y)
# Adjust the column names based on the actual structure of your DataFrame
# Assuming the columns for RGB values are named '93', '138', and '168'
X = df[['93', '138', '168']]
y = df['air_force_blue_raf']  # Adjust this label column based on your dataset

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
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the trained model for later use
model_filename = 'color_detection_model.joblib'
dump(rf_classifier, model_filename)
print(f'Model saved as {model_filename}')

# Optionally, you can print a classification report for more detailed evaluation
print('Classification Report:')
print(classification_report(y_test, y_pred))
 
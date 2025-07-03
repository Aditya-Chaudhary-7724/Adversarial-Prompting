import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load Dataset
df = pd.read_csv("adversarial_prompt_dataset.csv")

# ✅ Remove any rows where prompt or label is missing
df = df.dropna(subset=["prompt", "label"])

# ✅ Optional: remove empty strings
df = df[df["prompt"].str.strip() != ""]


# Step 2: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(df["prompt"], df["label"], test_size=0.2, random_state=42)

# Step 3: Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 4: Train a logistic regression classifier
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test_vec)

# Step 6: Evaluate
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Optional: Save the model
import joblib
joblib.dump(model, "prompt_classifier_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("\n✅ Model saved as 'prompt_classifier_model.pkl'")

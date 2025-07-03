import joblib

# Load model and vectorizer
model = joblib.load("prompt_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Take input
prompt = input("📝 Enter your prompt:\n> ")

# Predict
vec = vectorizer.transform([prompt])
proba = model.predict_proba(vec)[0]
confidence = max(proba) * 100
threshold = 60
prediction = model.predict(vec)[0]

# Apply threshold
if confidence < threshold:
    label = "uncertain"
else:
    label = prediction

# Output result
print(f"\n🔍 Predicted Label: {label}")
print(f"📊 Confidence: {confidence:.2f}%\n")

# Show all class-wise probabilities
classes = model.classes_
print("🔢 Class Probabilities:")
for i, cls in enumerate(classes):
    print(f"  - {cls}: {proba[i]*100:.2f}%")

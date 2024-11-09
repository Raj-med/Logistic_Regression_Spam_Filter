import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import pickle
import os


# Sample data (texts with spam labels)
data = {
    'text': [
        "Win a lottery now!", "Hello, let's meet for lunch", "Get rich fast!", 
        "Hey, did you finish the report?", "Claim your prize!", "Join us for a meeting",
        "This is not spam", "You are a winner!", "Meeting scheduled at 10 AM",
        "Congratulations! You've won a gift card!", "Can we reschedule our meeting?",
        "Free money awaits you!", "Let's catch up soon", "Earn money fast with this simple trick",
        "Please find attached the report", "Hurry up! Offer ends soon"
    ],
    'label': [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Vectorize text (convert text to numerical features)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


# Specify the full path where you want to save the files
save_path = "c:/CODING/working/"

# Save the trained model
with open(os.path.join(save_path, "model.pkl"), "wb") as model_file:
    pickle.dump(model, model_file)

# Save the vectorizer
with open(os.path.join(save_path, "vectorizer.pkl"), "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)



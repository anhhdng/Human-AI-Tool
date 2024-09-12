import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import pickle

# Example dataset (replace this with real data)
data = {
    'text': [
        "Patient exhibits symptoms of depression and anxiety.",
        "Diagnosed with type 2 diabetes mellitus.",
        "Severe acute respiratory syndrome.",
        "Hypertensive heart disease with heart failure.",
        "Chronic obstructive pulmonary disease with exacerbation."
    ],
    'icd10_code': [
        "F32",  # Major depressive disorder
        "E11",  # Type 2 diabetes mellitus
        "U07.1",  # COVID-19, virus identified
        "I11.0",  # Hypertensive heart disease with heart failure
        "J44.1"  # Chronic obstructive pulmonary disease
    ]
}

df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['icd10_code'], test_size=0.2, random_state=42)

# Create a pipeline that combines the vectorizer and the classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model as a pickle file
with open('models/icd10_model.pkl', 'wb') as f:
    pickle.dump(model, f)

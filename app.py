from flask import Flask, request, jsonify
import pickle
import os
import logging

app = Flask(__name__)

# Load the saved model and vectorizer
with open("model.pkl", "rb") as model_file, open("vectorizer.pkl", "rb") as vectorizer_file:
    model = pickle.load(model_file)
    vectorizer = pickle.load(vectorizer_file)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json.get("text", "")
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)[0]
    return jsonify({"prediction": "spam" if prediction == 1 else "not spam"})

if __name__ == "__main__":
    app.run(debug=True)


model_path = 'c:/CODING/working/model.pkl'
vectorizer_path = 'c:/CODING/working/vectorizer.pkl'

if not os.path.exists(model_path):
    print("Model file not found!")
if not os.path.exists(vectorizer_path):
    print("Vectorizer file not found!")

# Load model and vectorizer
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


# Enable logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get the incoming JSON data
        logging.debug(f"Received data: {data}")  # Log the incoming data
        text = data['text']  # Extract the 'text' field from the data
        
        if not text.strip():  # Check if the text is empty or contains only whitespace
            return jsonify({'error': 'Input text cannot be empty'}), 400
        
        # Make the prediction using the model
        prediction = model.predict([text])
        logging.debug(f"Prediction: {prediction}")  # Log the prediction result
        return jsonify({'prediction': prediction[0]})  # Return the prediction as a JSON response

    except Exception as e:  # Catch any exceptions
        logging.error(f"Error: {str(e)}")  # Log the error message
        return jsonify({'error': str(e)}), 500  # Return error response with status 500




# Spam Detection Model with API
![](https://github.com/Raj-med/Logistic_Regression_Spam_Filter/blob/main/logistic%20regression.gif)

This project will provide a REST API for detecting spam and non-spam text messages using a logistic regression model. The model is trained to classify text into two categories: **spam** and **not spam**. You can interact with the model through an HTTP API endpoint.

## Requirements

To run the project, you need to have the following installed:

- Python 3.x
- pip (Python package manager)

## Setup Instructions

1. Clone or download the repository to your local machine.

2. Install the required dependencies by running the following command in your terminal or command prompt:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that the model (`model.pkl`) and vectorizer (`vectorizer.pkl`) files are present in the project directory.

4. Start the Flask application by running:

    ```bash
    python app.py
    ```

5. The Flask API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### `/predict` (POST)

This endpoint receives a POST request with a JSON payload containing a "text" field. It returns a prediction of whether the text is spam or not spam.

**Request Example:**

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "Congratulations! You’ve won a $1000 gift card. Claim your prize now!"}'

## Response Example (Spam):
{
  "prediction": "spam"
}



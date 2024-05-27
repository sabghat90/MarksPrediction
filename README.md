# Student Performance Prediction

This project aims to predict student performance using various machine learning regression techniques. The model is integrated into a Flask web application to provide real-time predictions based on user input.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The objective of this project is to develop a predictive model that accurately forecasts students' academic performance. The project follows the standard machine learning pipeline, including data collection, EDA, preprocessing, model training, evaluation, and deployment.

## Data Collection

Student performance data was collected from multiple sources and ingested into the project. The data was meticulously checked for integrity and quality to ensure accurate model training and predictions.

## Exploratory Data Analysis (EDA)

Comprehensive EDA was conducted to uncover key patterns, trends, and correlations in the dataset. This step was crucial for understanding the data and informing feature selection and engineering.

## Data Preprocessing

Data preprocessing involved cleaning the data, handling missing values, scaling numerical features, and encoding categorical variables. These steps were essential to prepare the data for effective model training.

## Model Training

Several regression models were trained, including:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBRegressor
- CatBoost Regressor
- AdaBoost Regressor

Hyperparameter tuning was performed using GridSearchCV to optimize model performance.

## Model Evaluation

Models were evaluated based on their R2 score and other relevant metrics. The best-performing model was selected for deployment.

## Web Application

A Flask web application was developed to provide real-time predictions. Users can input relevant features, and the application will return the predicted performance.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/sabghat90/Score-Prediction.git
    cd Score-Predictioin
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage

To use the web application, navigate to `http://127.0.0.1:8080/` in your web browser. Fill in the required fields and click "Predict" to see the prediction results.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

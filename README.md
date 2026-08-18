# 🏠 House Price Prediction

A Machine Learning based web application that predicts house prices based on user-provided house features.

## 📌 Project Overview

This project uses Machine Learning to predict the price of a house based on features such as bedrooms, bathrooms, living area, lot area, floors, waterfront, view, condition, basement area, and year built.

The trained Machine Learning model is integrated into a Django web application.

## 🤖 Machine Learning

The following regression algorithms were tested:

- K-Nearest Neighbors (KNN)
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### 🏆 Best Model

Linear Regression performed best among the tested models.

**R² Score:** 0.448

**Mean Absolute Error:** 139,590

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Django
- HTML
- CSS
- Joblib

## 📊 Input Features

The application uses the following features:

- Bedrooms
- Bathrooms
- Living Area
- Lot Area
- Floors
- Waterfront
- View
- Condition
- Above Ground Area
- Basement Area
- Year Built

## 🌐 Web Application

The Django application allows users to:

1. Enter house details.
2. Submit the information.
3. Send the data to the trained Machine Learning model.
4. Predict the estimated house price.
5. Display the predicted price on the webpage.


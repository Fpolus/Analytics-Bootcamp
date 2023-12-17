# Credit Risk Analysis Report

## Overview

This analysis focuses on credit risk assessment using logistic regression. The dataset contains information about loans, and the goal is to predict whether a loan is healthy (0) or has a high risk of default (1).

## Data Loading and Preprocessing

- The lending data is loaded from the 'lending_data.csv' file in the 'Resources' folder.
- The data is separated into labels (y) and features (X).
- The balance of target values is checked, showing the count of each class in the target variable.

## Train-Test Split

- The data is split into training and testing sets using `train_test_split` from Scikit-Learn.

## Logistic Regression Model (Original Data)

- A logistic regression model is instantiated and fitted using the training data (X_train and y_train).
- Predictions are made on the testing data (X_test).
- Balanced accuracy, a confusion matrix, and a classification report are used to evaluate the model's performance.

## Handling Imbalanced Data

- The RandomOverSampler from imbalanced-learn is used to oversample the minority class in the training data.

## Logistic Regression Model (Oversampled Data)

- Another logistic regression model is instantiated and fitted using the resampled training data.
- Predictions are made on the testing data, and performance is evaluated using balanced accuracy, a confusion matrix, and a classification report.

## Evaluation Metrics

- Balanced accuracy, confusion matrix, and classification report metrics are printed for both the original and oversampled models.

## Results

**scores are directly pulled from the oversampled data**

- **Accuracy Score:** 99%
- **Precision Score:**
  - Healthy Loans (Class 0): 100%
  - High-Risk Loans (Class 1): 84%
- **Recall Score:**
  - Healthy Loans (Class 0): 99%
  - High-Risk Loans (Class 1): 99%



## Summary

The logistic regression models showcase outstanding performance in predicting both healthy and high-risk loans. Specifically:

- **Healthy Loans (Class 0):**
  - The model achieves perfect precision and high recall, signifying accurate identification and capture of non-risky loans.
- **High-Risk Loans (Class 1):**
  - While precision is slightly lower at 84%, the model maintains excellent recall, indicating effective identification of most actual high-risk loans.

## Analysis

The high accuracy and balanced precision-recall scores suggest the models effectively differentiate between healthy and high-risk loans. The precision-recall trade-off is well-managed, with minimal false positives and strong recall for high-risk cases.

## Recommendation

The logistic regression models, trained on both normal and oversampled datasets, demonstrate robust performance in credit risk prediction. The decision to use these models depends on business priorities:

- **Normal Model:**
  - Achieves high accuracy and precision-recall scores.
  - Suitable for scenarios where minimizing false positives (misclassification of healthy loans as high-risk) is a priority.

- **Oversampled Model:**
  - Slightly lower precision but with enhanced recall for high-risk loans.
  - Effective in minimizing both false positives and false negatives.

Consideration of business objectives will guide the selection between the normal and oversampled models. Further fine-tuning and monitoring may be undertaken based on evolving data patterns.

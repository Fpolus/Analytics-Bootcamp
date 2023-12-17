# AlphabetSoupCharity Neural Network Model

---

## Overview of the Analysis

The purpose of this analysis was to create a deep learning model using TensorFlow and Keras to predict whether an Alphabet Soup-funded organization would be successful based on the provided dataset. The process involved data preprocessing, model design, training, evaluation, optimization, and reporting on the model's performance.

## Results

### Data Preprocessing

- **Target Variable(s)** 
- **Feature Variable(s)** 
- **Removed Variables** 

### Compiling, Training, and Evaluating the Model

- **Neurons, Layers, and Activation Functions:** 
  - **Neural Network Structure:** The model architecture consisted of a deep neural network with:
    - Input features: [Number of input features: `25724`].
    - Hidden Layer 1: [Number of neurons: `7`], Activation: ReLU.
    - Hidden Layer 2: [Number of neurons: `14`], Activation: ReLU.
    - Output Layer: 1 neuron, Activation: Sigmoid.
  - **Reasoning behind Choices:** The input layer was determined by the number of features in the training data. The subsequent hidden layers' sizes were chosen to incrementally widen representation capacity.
- **Achieving Target Performance:** Over 75% accuracy was attained after 2 optimizations.
- **Steps to Increase Performance:** Optimization steps included:
  - Adjusting input data by [describe modifications].
  - Adding neurons and layers.
  - Experimenting with activation functions.
  - Varying epochs during training.

 

## Summary

The deep learning model successfully predicted whether Alphabet Soup-funded organizations would be successful with over 75% accuracy after several optimization attempts. The iterative process involved adjusting data preprocessing steps, altering the neural network architecture, and experimenting with various hyperparameters. A different approach to solving this classification problem could involve using a different type of model, such as a Random Forest Classifier or a Gradient Boosting Classifier. These models could potentially capture non-linear relationships and interactions between features differently compared to a neural network, providing an alternative solution worth exploring.

---

## Instructions

### Steps Completed:

1. **Data Preprocessing:** 
   - Read in the dataset 'charity_data.csv' using Pandas.
   - Identified target and feature variables.
   - Dropped 'EIN' and 'NAME' columns.
   - Analyzed unique values in columns and binned rare occurrences.
   - Encoded categorical variables using pd.get_dummies().
   - Split the data into training and testing datasets.
   - Scaled the features using StandardScaler from scikit-learn.

2. **Model Compilation, Training, and Evaluation:** 
   - Designed a neural network using TensorFlow and Keras.
   - Configured layers, neurons, and activation functions.
   - Compiled and trained the model on the training data.
   - Evaluated model performance using the test dataset.
   - Saved the model's weights every five epochs.

3. **Model Optimization:** 
   - Made several attempts to optimize the model:
     - Adjusted input data, including dropping or binning columns.
     - Modified neural network architecture (layers, neurons, activations).
     - Varied hyperparameters such as epochs during training.

### Files Included:

- `AlphabetSoupCharity.h5`: File containing the trained neural network model.
- `AlphabetSoupCharityOptimized.h5`: File containing an optimized neural network model achieving over 75% accuracy.

### Conclusion:

The neural network model successfully predicts the success of Alphabet Soup-funded organizations with over 75% accuracy. The optimization process involved several iterations and adjustments to achieve this target performance. The repository provides a comprehensive guide to understand and replicate the workflow, serving as a foundation for further improvements or alternative modeling approaches.

# Cryptocurrency Clustering with K-Means and PCA

This repository contains code and analysis for clustering cryptocurrencies using the K-Means algorithm and Principal Component Analysis (PCA). The analysis is conducted on the original data and then compared with results obtained after reducing the dimensionality using PCA.

## Table of Contents

1. [Introduction](#introduction)
2. [Elbow Method and Clustering with Original Data](#elbow-method-and-clustering-with-original-data)
3. [Clustering Optimization with PCA](#clustering-optimization-with-pca)
4. [Coding Conventions and Formatting](#coding-conventions-and-formatting)
5. [Deployment and Submission](#deployment-and-submission)
6. [Code Comments](#code-comments)

## Introduction

The goal of this project is to cluster cryptocurrencies based on their price change percentages over a specific time period using K-Means clustering. Additionally, Principal Component Analysis (PCA) is employed to reduce the dimensionality of the dataset and improve clustering accuracy.

## Elbow Method and Clustering with Original Data

### 1. Elbow Method

To determine the optimal number of clusters (k), the elbow method was implemented. The range of k was set from 1 to 11, and the inertia values were plotted to find the "elbow point."

### 2. Clustering with Original Data

The K-Means model was initialized with the best value for k obtained from the elbow method. The clusters were predicted and added as a new column to the original data. A scatter plot was generated using hvPlot, with points colored by the cluster labels.

## Clustering Optimization with PCA

### 3. Principal Component Analysis (PCA)

A PCA model with three components was created to reduce the dimensionality of the dataset. The explained variance was analyzed to understand the contribution of each principal component.

### 4. Elbow Method with PCA Data

The elbow method was applied to the PCA data to find the optimal k for clustering. The inertia values were plotted to visualize the elbow point.

### 5. Clustering with PCA Data

The K-Means model was initialized with the optimal k from PCA. The clusters were predicted and added to the PCA data. A scatter plot was generated using hvPlot to visualize the clusters.

## Coding Conventions and Formatting

- Imports are placed at the top of the file.
- Functions and variables are named with lowercase characters and words separated by underscores.
- DRY principles are followed to create maintainable and reusable code.
- Concise logic and creative engineering are used where possible.

## Deployment and Submission

1. [GitHub Repository](<https://github.com/Fpolus/CryptoClustering>)
2. Use the command line to add files to the repository.
3. Include appropriate commit messages in your files.

## Code Comments

The code is well-commented with concise, relevant notes to aid other developers in understanding the implemented algorithms and steps.

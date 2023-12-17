# Home Sales Data Analysis

This repository contains PySpark SQL code for analyzing home sales data. The Home_Sales.ipynb notebook delves into the dataset (home_sales_revised.csv) to perform a range of analyses using PySpark functions.

## Overview

- **Home_Sales.ipynb**: Jupyter Notebook with PySpark code for data analysis.
- **home_sales_revised.csv**: CSV file with home sales data.
- **formatted_home_sales/**: Directory housing formatted data partitioned by the date built in Parquet format.

## Tasks Completed

- **File Renaming**: Renamed the notebook file to Home_Sales.ipynb.
- **Data Import**: Read the CSV data into a Spark DataFrame.
- **Temporary Tables**: Created home_sales and parquet_home_sales tables for analysis.
- **Querying**: Answered specific questions using SparkSQL queries.
- **Performance Evaluation**: Cached and uncached tables to compare query runtimes.
- **Data Storage**: Partitioned and stored formatted data in Parquet format for optimization.
- **Data Analysis**: Explored criteria such as bedrooms, bathrooms, price, and view ratings.

## Instructions

### Setup

Ensure Home_Sales.ipynb and home_sales_revised.csv are in the same directory.

### Environment

Configure the PySpark environment to run the notebook.

### Execution

Run notebook cells sequentially for analysis and query execution.

### Customization

Modify file paths or criteria for different datasets or specific analyses.

---


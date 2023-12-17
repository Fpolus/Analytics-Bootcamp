# UK Food Establishments Database Analysis

---

This repository contains the code and data for analyzing the UK Food Establishments Database. The analysis involves setting up a MongoDB database, updating it with new information, and conducting exploratory analysis to answer specific questions. This project is in response to a challenge from Eat Safe, Love magazine.

# Part 1: Database and Jupyter Notebook Setup

Importing Data
I imported the data from the establishments.json file into a MongoDB database named uk_food, and created a collection named establishments. Below is the command used to import the data:

bash
Copy code

mongoimport --db uk_food --collection establishments --file establishments.json

Libraries Used
In my Jupyter Notebook, I imported the following libraries:

pymongo for connecting to MongoDB.
pprint for pretty printing MongoDB documents.
Database Confirmation

I confirmed the successful setup of the database by:

Listing the databases in MongoDB, verifying the presence of uk_food.
Listing the collections in the uk_food database, confirming the presence of establishments.
Retrieving and displaying one document from the establishments collection using find_one.
Part 2: Database Update
New Restaurant Addition
I added a new restaurant, "Penang Flavours," to the database with the provided information. This restaurant is located in Greenwich and has a pending rating.

---

# BusinessTypeID Update

I found the BusinessTypeID for "Restaurant/Cafe/Canteen" and updated the new restaurant's document with this information.

# Removal of Dover Establishments

I identified and removed all establishments within the Dover Local Authority from the database.

# Data Type Conversion

I converted specific number values stored as strings to decimal numbers for latitude and longitude and to integer numbers for RatingValue.

# Part 3: Exploratory Analysis

I conducted an exploratory analysis of the database to answer the following questions:

---

Which establishments have a hygiene score equal to 20?

There are 41 establishments with a hygiene score equal to 20.

---

Which establishments in London have a RatingValue greater than or equal to 4?

There are 33 establishments in London with a RatingValue greater than or equal to 4.

---

What are the top 5 establishments with a RatingValue of 5, sorted by the lowest hygiene score, nearest to "Penang Flavours"?

The top 5 establishments with a RatingValue of 5, sorted by the lowest hygiene score, nearest to "Penang Flavours" are:
Volunteer
Plumstead Manor Nursery
Atlantic Fish Bar
Iceland
Howe and Co Fish and Chips - Van 17
How many establishments in each Local Authority area have a hygiene score of 0?

---

There are a total of 55 establishments with a hygiene score of 0 across various Local Authority areas. The top ten Local Authority areas with the most establishments having a hygiene score of 0 are displayed in the analysis.

The results of these analyses were presented in the Jupyter Notebook using Pandas DataFrames and were also displayed as Markdown cells in the document.

---

# Acknowledgments

I would like to acknowledge the various resources that contributed to the completion of this assignment. I made use of a range of learning materials, including class resources and online references, which collectively aided me in successfully finishing this project.

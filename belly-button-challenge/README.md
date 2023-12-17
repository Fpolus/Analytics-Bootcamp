# Belly Button Biodiversity Dashboard


## Overview

The Belly Button Biodiversity Dashboard is an interactive web application designed to explore and visualize a dataset related to the biodiversity of belly button microbes. This project provides users with a user-friendly interface to access and analyze the dataset, including demographic information for different test subjects and visualizations of bacteria cultures found in their belly buttons.

### Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

### Live Demo

Check out the live demo [here](https://fpolus.github.io/belly-button-challenge/).

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/fpolus/belly-button-challenge.git

Navigate to the project directory:

cd belly-button-challenge
Open the project in your preferred code editor.

Run a local development server or open the index.html file in your web browser.

## Usage

Select a test subject ID from the dropdown menu to view data for that individual.

Explore the following visualizations and information:

Bar Chart: Displays the top 10 Operational Taxonomic Units (OTUs) found in the selected individual. Uses sample values as bar heights, OTU IDs as labels, and OTU labels as hover text.

Bubble Chart: Shows each sample's OTU IDs on the x-axis and sample values on the y-axis. The marker size represents the sample values, and marker colors correspond to OTU IDs. Hover over the data points to see OTU labels.

Demographic Info: Presents demographic information for the selected individual.

The visualizations and demographic info will update when a new sample is selected from the dropdown menu.

## Project Structure

The project structure is organized as follows:

- index.html            # Main HTML file
- static/
  - js/
    - app.js            # JavaScript code for data visualization and interactivity
- README.md             # Project documentation
- samples.json          # Data source

## Technologies Used

JavaScript: The application's core logic is written in JavaScript, making it interactive and dynamic.

D3.js: D3.js (Data-Driven Documents) is used for data manipulation and binding data to visual elements.

Plotly: Plotly is utilized to create interactive and responsive data visualizations, including the bar chart, bubble chart, and gauge chart.



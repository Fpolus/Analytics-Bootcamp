# Earthquake Map Visualization
This project demonstrates the visualization of earthquake data using Leaflet and D3.js. The code creates an interactive map that displays earthquake locations, magnitudes, and depths, allowing users to explore earthquake information easily.

# Prerequisites
Before running this code, make sure you have the following dependencies installed:

Leaflet: A popular JavaScript library for interactive maps.
D3.js: A JavaScript library for data visualization.
Internet connection for accessing the earthquake data from the USGS API.

# Getting Started
Download or clone this repository to your local machine.
Open the index.html file in a web browser.

# Code Structure
## HTML
The HTML file (index.html) defines the structure of the web page and includes references to external resources (Leaflet and D3.js libraries).
## JavaScript (static/js/logic.js)
### queryUrl: 
This variable stores the URL of the USGS Earthquake API, which provides earthquake data for the past week.

### chooseColor(depth): 
A function that returns a color based on the depth of an earthquake. It uses a range of colors to represent different depth levels.

The code uses D3.js to perform a GET request to the USGS API and retrieve earthquake data. The retrieved data is logged to the console.

### onEachFeature(feature, layer): 
A function used to bind popups to each earthquake location on the map. It displays information such as location, date, magnitude, and depth.

### chooseRadius(magnitude): 
A function that calculates the radius of the circle markers on the map based on earthquake magnitude.

The earthquake data is processed and added to the map as GeoJSON layers. Each earthquake is represented as a circle marker with different colors and sizes based on its depth and magnitude.

### createMap(earthquakes): 
This function creates the map and adds base layers and overlay layers. It also includes a legend that explains the color-coding used for earthquake depths.

## CSS (static/css/style.css)
The CSS file contains styles for the map and legend.
# Usage
Open index.html in a web browser to view the interactive earthquake map.
You can click on the earthquake markers to see more information about each earthquake.
The legend on the bottom right of the map explains the colors used for representing earthquake depths.
# Note
This code assumes an internet connection to fetch earthquake data from the USGS API.
Make sure your web browser allows loading external resources (Leaflet and D3.js libraries).
# Authors
[Frank Polus]
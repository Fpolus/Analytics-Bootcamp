// Store our API endpoint as queryUrl.
let queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

function chooseColor(depth) {
    return depth > 200 ? '#800026' :
           depth > 90 ? '#bd0026' :
           depth > 70 ? '#d73027' :
           depth > 50 ? '#fc8d59' :
           depth > 30 ? '#fee08b' :
           depth > 10 ? '#d9ef8b' :
           depth < 10 ? '#91cf60' :
                        '#1a9850';
  }

// Perform a GET request to the query URL.
d3.json(queryUrl).then(function (data) {
  console.log(data);

  // console.log(data.features);

  // Using the features array sent back in the API data, create a GeoJSON layer, and add it to the map.

  // 1.
  // Pass the features to a createFeatures() function:
//   createFeatures();

function onEachFeature(feature, layer) {
  layer.bindPopup(
      "<h3>" + feature.properties.place + "</h3><hr>" +
      "<p>" + new Date(feature.properties.time) + "</p>" +
      "<p>" + feature.properties.mag + " Magnitude</p>" +
      "<p>" + feature.geometry.coordinates[2] + " Depth</p>"
  );
}


function chooseColor(depth) {
  return depth > 200 ? '#800026' :
         depth > 90 ? '#bd0026' :
         depth > 70 ? '#d73027' :
         depth > 50 ? '#fc8d59' :
         depth > 30 ? '#fee08b' :
         depth > 10 ? '#d9ef8b' :
         depth < 10 ? '#91cf60' :
                      '#1a9850';
}

  function chooseRadius(magnitude) {
    return magnitude * 5;
  }

  let earthquakes = L.geoJSON(data.features, {
    style: function (feature) {
      return {
        color: "white",
        fillColor: chooseColor(feature.geometry.coordinates[2]),
        fillOpacity: 0.5,
        radius: chooseRadius(feature.properties.mag),
        weight: 1.5
      };
    },
    onEachFeature: onEachFeature,
    pointToLayer: function (feature, latlng) {
        let depthValue = feature.geometry.coordinates[2];
        console.log("Depth:", depthValue);
        
        return L.circleMarker(latlng, {
            radius: chooseRadius(feature.properties.mag),
            fillColor: chooseColor(depthValue),
            color: "white",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.5
        });
    }

    
  });
  

    createMap(earthquakes);
  });

// 3.
// createMap() takes the earthquake data and incorporates it into the visualization:

function createMap(earthquakes) {
  // Create the base layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  // Create a baseMaps object.
  let baseMaps = {
    "Street Map": street
  };

  // Create an overlays object.
  let overlayMaps = {
    Earthquakes: earthquakes,
  };

  // Create a new map.
  // Edit the code to add the earthquake data to the layers.
  let myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street, earthquakes]
  });

  // Create a layer control that contains our baseMaps.
  // Be sure to add an overlay Layer that contains the earthquake GeoJSON.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

  var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
            grades = [-10, 10, 30, 50, 70, 90]

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + chooseColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };

    legend.addTo(myMap);

}
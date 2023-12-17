// 14-Interactive-Web-Visualizations/02-Homework/Instructions/StarterCode/static/js/app.js
let url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json"

// create the displayCharts function to display the charts and panel
function displayCharts(id) {
     // we do no have access to data here
    // we need to get the data again
    d3.json(url).then(function(data) {
        samples = data.samples;
        console.log(samples);
    
        // filter the data to get the sample values, otu_ids, and otu_labels for the id
        let selectedSample = samples.filter(sample => sample.id == id);
        console.log(selectedSample);

        // get the top 10 otu ids and reverse them for the plotly
        otuIds = selectedSample[0].otu_ids;
        otuLabels = selectedSample[0].otu_labels;
        sampleValues = selectedSample[0].sample_values;

        console.log(otuIds);

        // get the top 10 otu ids and reverse them for the plotly
        let topOtuIds = otuIds.slice(0,10).reverse();
        let topOtuLabels = otuLabels.slice(0,10).reverse();
        let topSampleValues = sampleValues.slice(0,10).reverse();

        console.log(topOtuIds);

        // create the trace for the bar chart
        let trace1 = {
            x: topSampleValues,
            y: topOtuIds.map(otuId => `OTU ${otuId}`),
            text: topOtuLabels,
            type: "bar",
            orientation: "h"
        };

        // create the data array for the bar chart
        let barData = [trace1];

        // define the bar plot layout
        let barLayout = {
            title: "Top 10 Bacteria Cultures Found",
            margin: {t: 30, l: 150}
        };

        // plot the bar chart
        Plotly.newPlot("bar", barData, barLayout);

        // create the trace for the bubble chart
        let trace2 = {
            x: otuIds,
            y: sampleValues,
            text: otuLabels,
            mode: "markers",
            marker: {
                size: sampleValues,
                color: otuIds,
                colorscale: "Earth"
            }
        };

        // create the data array for the bubble chart
        let bubbleData = [trace2];

        // define the bubble plot layout
        let bubbleLayout = {
            title: "Bacteria Cultures Per Sample",
            xaxis: {title: "OTU ID"},
            margin: {t: 30}
        };

        // plot the bubble chart
        Plotly.newPlot("bubble", bubbleData, bubbleLayout);

        // get the metadata for the selected id
        let metadata = data.metadata;

        // filter the data to get the metadata for the id
        let selectedMetadata = metadata.filter(sample => sample.id == id);

        console.log(selectedMetadata);

        // select the panel to put the data
        let panel = d3.select("#sample-metadata");

        // clear the panel
        panel.html("");

        // add each key and value pair to the panel
        Object.entries(selectedMetadata[0]).forEach(([key, value]) => {
            panel.append("h6").text(`${key}: ${value}`);
        });
    });
}

// create the optionChanged function to get the new id when the dropdown menu is changed
function optionChanged(selectedId) {
    // display the id in the console
    displayCharts(selectedId);

}

// create the init function to display the charts and data
function init () {

    // get the data
    d3.json(url).then(function(data) {

        // display the data in the console
        console.log(data);

        // get the ids for the dropdown menu
        let dropdownMenu = d3.select("#selDataset");

        // get the ids from the data
        let ids = data.names;

        // display the ids in the console
        for (let i = 0; i < ids.length; i++) {

            // append the ids to the dropdown menu
            dropdownMenu.append("option").text(ids[i]).property("value", ids[i]);
        }

        // get the first id
        first = ids[0];

        // Display the charts and panel with the first ID
        displayCharts(first);

    });
}

// call the init function
init();




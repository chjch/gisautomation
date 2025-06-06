# Resilient Symposium 2025

- Workshop: **Unlocking Global Demographic Insights with GeoEnrichment and Agentic AI Coding**
- Speaker: Changjie Chen, chj.chen@ufl.edu
- Location: University of Cuenca, Ecuador
- Date: 2025.06.06

## Agenda

1. Overview of GeoEnrichment service
2. Using GeoEnrichment with Python in Google Colab
3. Develop a web application featuring GeoEnrichment in Cursor, an Agentic AI coding experience

## 1. What is GeoEnrichment?

[**GeoEnrichment**](https://www.esri.com/en-us/arcgis/products/arcgis-location-platform/services/geoenrichment), also known as _Data Enrichment_, is one of the services (tools) provided by Esri's ArcGIS Location Platform. It is the process of finding demographic data and local facts for locations around the world. 

This cloud-based service allows you to access global demographic, socioeconomic, and lifestyle data **in seconds**. The additional information can drive better understanding, analysis, and decision-making.

![data-enrichment-gif](_static/images/data-enrichment.gif)

```{admonition} Use Cases

- Interactively explore any area of interest.
- Automate and simplify the process social, economic, and demographic data collection.
- Access more data beyond Census, including _Jobs_, _Behaviors_, _Spending_, _Crime_, and _Health_ data.
```

Check out this [live example](https://chjch.github.io/gisautomation/_static/geoenrichment.html).

## 2. Using GeoEnrichment in Google Colab

### 2.1 How to access GeoEnrichment service

To perform GeoEnrichment, we need to utilize Esri's [GeoEnrichment service](https://developers.arcgis.com/documentation/mapping-and-location-services/data-enrichment/#api-support). The service provides over **15,000** data variables (data fields) with coverage for more than 150 countries and regions. 

An **access token** is _required_ to use the service for developers who have an [ArcGIS Location Platform](https://developers.arcgis.com/documentation/glossary/arcgis-location-platform-account/) account or [ArcGIS Online account](https://developers.arcgis.com/documentation/glossary/arcgis-online-account/).

The service can be used with many Esri APIs (Application Programming Interfaces), such as _ArcGIS Maps SDK_ and _ArcGIS REST JS_. Among them, only ArcGIS Python API offers [Full Support](https://developers.arcgis.com/documentation/mapping-and-location-services/data-enrichment/#api-support).

:::{admonition} API Key (for this workshop only)

```bash
AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF
```
:::

Refer to [this](https://chjch.github.io/gisautomation/modules/7-2.geoenrichment.html#user-authentication) for more details on user authentication and creating an access token.

### 2.2 Create a Notebook in Google Colab

```{figure} _static/images/Google_Colaboratory_SVG_Logo.svg
:name: google-colab-logo
:alt: Google Colab Logo
:width: 200px
:class: mb-3
:align: right
```

[Google Colab](https://colab.research.google.com/) is a free, cloud-based Jupyter notebook environment that requires no setup. It provides:
- Free access to GPUs and TPUs
- Pre-installed data science libraries
- Easy sharing and collaboration
- Integration with Google Drive

```{admonition} Access Google Colab
:class: tip

Navigate to https://colab.research.google.com to create a new notebook.
You can also go to Google Drive first and then click on the "New" button and then "Google Colaboratory" to create a new notebook.
If you have multiple Google accounts, you can switch to the account you want by use the `authuser` parameter. For example,
https://colab.research.google.com/?authuser=1
```

To get started, we'll install the [ArcGIS API for Python](https://developers.arcgis.com/python/) and its dependencies.

```python
!pip install numpy==1.24.3
!pip install arcgis
!pip install arcgis-mapping
```

Copy the above code to the first **cell** of the notebook and run it. You can do that by clicking on the **Run** button (at the beginning of the cell) or pressing `Shift + Enter`.

:::{admonition} ArcGIS API for Python
:class: tip

```{figure} _static/images/APIforPython.png
:name: api for python
:alt: api for python
:width: 100px
:align: right
```

The ArcGIS API for Python, i.e., the `arcgis` package, is a powerful, modern and easy to use Pythonic library to perform GIS visualization and analysis, spatial data management and GIS system administration tasks that can run both in an interactive fashion, and using scripts.

The package is shipped with a standard ArcGIS Pro installation. The API is distributed as the `arcgis` package via **conda** and **pip**. Within the `arcgis` package, which represents the generic GIS model, functionality is organized into a number of different modules that makes it simple to use and understand. Each module has a handful of types and functions that are focused towards one aspect of the GIS.
:::

Now let's add the API key to the notebook.

```python
from arcgis.gis import GIS

api_key="AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF"

gis = GIS(api_key=api_key)
```

We have successfully created a GIS object. Now what can GIS do? Right, we use GIS to create maps.

```python
map = gis.map()
map
```

Congratulations! You have just created a map in your browser using Python.

Now let's do some configuration to the map.

```python
map.basemap.basemap = "arcgis-navigation"  # set the basemap
map.center = [-2.900060, -79.009290]       # set the map's center
map.zoom = 12                              # set the zoom level
```

We have centered the map at the coordinates of UCuenca. Let's add that point to the map.

```python
from arcgis.geometry import Point

pt = Point({
    "x": -79.009290,   # longitude
    "y": -2.900060,    # latitude
    "spatialReference": {"wkid":4326} # WGS84
})

map.content.draw(pt)   # draw the point
```

Now, let's figure out how many people live within 0.5, 1, and 2 kilometers from the point. To do that, we need to use the `enrich` function from the `arcgis.geoenrichment` module.

```python
# import pandas to store the results
import pandas as pd
from arcgis.geoenrichment import BufferStudyArea, enrich
from arcgis.mapping import PopupInfo

buffered = BufferStudyArea(area=pt, radii=[500, 1000, 2000], units='Meters')

#enrich using keyglobalfacts data collection and return geometry
result_data_frame = enrich(
    study_areas=[buffered], 
    data_collections=['KeyFacts'],
    return_geometry=False  # skip returning geometry
)
result_data_frame
```

Now let's put those buffers on the map and add the population information to the **Popup**.

```python
from arcgis.map.popups import PopupInfo

result_data_frame = enrich(
    study_areas=[buffered], 
    data_collections=['KeyFacts'],
    return_geometry=True  # return geometry to display on map
)

# Draw each buffer with PopupInfo
for i in range(len(result_data_frame)):
    popup = PopupInfo(
        title=f"Buffer {result_data_frame.buffer_radii.iloc[i]}m",
        description=f"Total Population: {result_data_frame.totpop.iloc[i]}"
    )
    map.content.draw(result_data_frame.SHAPE.iloc[i], popup=popup)
```

### 2.3 How does GeoEnrichment work

The GeoEnrichment service uses a **Data Apportionment** algorithm to redistribute demographic, data to input polygon features the user defined. The algorithm analyzes each polygon to be enriched relative to a point dataset (settlements) and a detailed dataset of reporting unit polygons that contain attributes for the selected variables. Based on how each polygon being enriched overlays these datasets, the algorithm determines the appropriate amount of each variable to assign.

```{figure} _static/images/data_apportionment.png
:name: data-apportionment
:alt: data-apportionment
:width: 50%
:align: center
```

```{admonition} Note
:class: tip

The GeoEnrichment service uses a **dasymetric apportionment technique** to aggregate census based demographic data for smaller areas. If areas are very small and do not intersect any census block data the service returns zero values. The GeoEnrichment service provides an estimate of population and does not count roof tops.
```

$$
w_i = \sum_{B \in P_i \cap T} W_i(B)
$$
Here, $B$ is a block and $W_i(B)$ is a weight of this block in the site $P_i$ which equals to,

$$
W_i(B) = \frac{V^{\text{TOTPOP}}(B)}{\sum_{B' \in P_i} V^{\text{TOTPOP}}(B')}.
$$

For more details, please refer to the [Apportionment Methodology](https://developers.arcgis.com/rest/geoenrichment/data-apportionment/#apportionment-methodology).

## 3. Develop a Web App with Cursor

```{figure} _static/images/cursor.svg
:name: cursor
:alt: cursor
:width: 100px
:align: right
```

[Cursor](https://www.cursor.com/) is an Integrated Development Environment (IDE), or simply a code editor, built on top of [Visual Studio Code](https://code.visualstudio.com/), designed with AI assistance at its core. It offers developers tools to **generate**, **refactor**, and navigate code more efficiently using **integrated language models** (e.g., GPT-4o, claude-4-sonnet, gemini-2.5-pro, etc.). By understanding the structure and context of your codebase, Cursor aims to streamline common development tasks without requiring you to leave your editor.

With features like _in-line code suggestions_, **intelligent search**, and **natural language explanations**, Cursor is intended to support developers in writing, reviewing, and maintaining code. Its goal is not to replace traditional workflows, but to enhance productivity and reduce friction in the software development process.

Navigate to [Cursor](https://www.cursor.com/) and sign up for a free account to download the software.

### 3.1 Create a web map using prompts

In the Agent mode, you can ask Cursor to create a web map using prompts. Note that we'll be creating a self-contained **HTML** file with **CSS** and **JavaScript** embedded in it.

Our web map is built on top of [ArcGIS Maps SDK for JavaScript](https://developers.arcgis.com/javascript/), which is a powerful tool for creating interactive maps.

Let's try with the following prompt:

```text
Create a web map using ArcGIS Maps SDK for JavaScript 4.32. The map should be centered at the coordinates of UCuenca, Ecuador.
```

This is the result:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>UCuenca Map</title>

    <link rel="stylesheet" href="https://js.arcgis.com/4.32/esri/themes/light/main.css">
    <script src="https://js.arcgis.com/4.32/"></script>

    <style>
        html,
        body,
        #viewDiv {
            padding: 0;
            margin: 0;
            height: 100%;
            width: 100%;
        }
    </style>

    <script>
        require([
            "esri/Map",
            "esri/views/MapView"
        ], function(Map, MapView) {
            // Create a Map instance
            const map = new Map({
                basemap: "topo-vector"
            });

            // Create a MapView instance
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-78.9875, -2.9006], // Coordinates of Universidad de Cuenca
                zoom: 15
            });
        });
    </script>
</head>

<body>
    <div id="viewDiv"></div>
</body>
</html>
```

:::{admonition} Extension
:class: tip

```{figure} _static/images/live_server.png
:name: live-server
:alt: live-server
:width: 100px
:align: right
```

Click on the **Extension** icon in the left sidebar and search for **Live Server** to install the extension. The live server will start a **local server** and allow you to see your web map in your defalut web browser.

There are many other great extensions in the Marketplace to make your coding experience more efficient and productive.
:::

### 3.2 Add api key and change the basemap

Try the following prompt:

```text
My api key is AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF

Please make the default basemap "arcgis/navigation", the exact name of the basemap.
```

### 3.3 Add GeoEnrichment service

Now let's add a toolbar to the map with the following prompt:

```text
Add the sketch widget to the top right of the map.
```

And this is the result:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>UCuenca Map</title>

    <link rel="stylesheet" href="https://js.arcgis.com/4.32/esri/themes/light/main.css">
    <script src="https://js.arcgis.com/4.32/"></script>

    <style>
        html,
        body,
        #viewDiv {
            padding: 0;
            margin: 0;
            height: 100%;
            width: 100%;
        }
    </style>

    <script>
        require([
            "esri/Map",
            "esri/views/MapView",
            "esri/config",
            "esri/widgets/Sketch",
            "esri/layers/GraphicsLayer"
        ], function(Map, MapView, esriConfig, Sketch, GraphicsLayer) {
            // Set the API key
            esriConfig.apiKey = "AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF";

            // Create a graphics layer for the sketch widget
            const graphicsLayer = new GraphicsLayer();

            // Create a Map instance
            const map = new Map({
                basemap: "arcgis/navigation",
                layers: [graphicsLayer]
            });

            // Create a MapView instance
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-78.9875, -2.9006], // Coordinates of Universidad de Cuenca
                zoom: 15
            });

            // Create the sketch widget
            const sketch = new Sketch({
                view: view,
                layer: graphicsLayer,
                creationMode: "hybrid"
            });

            // Add the sketch widget to the top right of the view
            view.ui.add(sketch, "top-right");
        });
    </script>
</head>

<body>
    <div id="viewDiv"></div>
</body>
</html>
```

Let's add the GeoEnrichment service to the map.

```text
when a point is being clicked I want to run the GeoEnrichment service using the point is center and with 500, 1000, and 2000 meter buffers to query "KeyFacts" about these polygons. using my api key and the ArcGIS REST API to make the request to the service.
```

Here is the result:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>UCuenca Map</title>

    <link rel="stylesheet" href="https://js.arcgis.com/4.32/esri/themes/light/main.css">
    <script src="https://js.arcgis.com/4.32/"></script>

    <style>
        html,
        body,
        #viewDiv {
            padding: 0;
            margin: 0;
            height: 100%;
            width: 100%;
        }
        #infoDiv {
            background-color: white;
            padding: 10px;
            width: 300px;
            position: absolute;
            top: 15px;
            left: 15px;
            z-index: 2;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
    </style>

    <script>
        require([
            "esri/Map",
            "esri/views/MapView",
            "esri/config",
            "esri/widgets/Sketch",
            "esri/layers/GraphicsLayer",
            "esri/Graphic",
            "esri/geometry/Point",
            "esri/geometry/Polygon",
            "esri/geometry/geometryEngine",
            "esri/symbols/SimpleFillSymbol",
            "esri/symbols/SimpleLineSymbol",
            "esri/Color"
        ], function(Map, MapView, esriConfig, Sketch, GraphicsLayer, Graphic, Point, Polygon, geometryEngine, SimpleFillSymbol, SimpleLineSymbol, Color) {
            // Set the API key
            esriConfig.apiKey = "AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF";

            // Create a graphics layer for the sketch widget and buffers
            const graphicsLayer = new GraphicsLayer();

            // Create a Map instance
            const map = new Map({
                basemap: "arcgis/navigation",
                layers: [graphicsLayer]
            });

            // Create a MapView instance
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-78.9875, -2.9006], // Coordinates of Universidad de Cuenca
                zoom: 15
            });

            // Create the sketch widget
            const sketch = new Sketch({
                view: view,
                layer: graphicsLayer,
                creationMode: "hybrid"
            });

            // Add the sketch widget to the top right of the view
            view.ui.add(sketch, "top-right");

            // Create info div
            const infoDiv = document.createElement("div");
            infoDiv.id = "infoDiv";
            infoDiv.innerHTML = "<h3>Buffer Analysis</h3><p>Click a point to see KeyFacts for different buffer zones.</p>";
            view.ui.add(infoDiv, "top-left");

            // Function to create buffer and query GeoEnrichment
            async function analyzePoint(point) {
                const buffers = [500, 1000, 2000]; // Buffer distances in meters
                let results = [];

                // Clear previous graphics
                graphicsLayer.removeAll();

                // Add the clicked point
                const pointGraphic = new Graphic({
                    geometry: point,
                    symbol: {
                        type: "simple-marker",
                        style: "circle",
                        color: "red",
                        size: "8px"
                    }
                });
                graphicsLayer.add(pointGraphic);

                // Create buffers and query for each
                for (const distance of buffers) {
                    // Create buffer
                    const buffer = geometryEngine.buffer(point, distance, "meters");
                    
                    // Create buffer graphic
                    const bufferGraphic = new Graphic({
                        geometry: buffer,
                        symbol: new SimpleFillSymbol({
                            color: new Color([0, 0, 255, 0.1]),
                            outline: new SimpleLineSymbol({
                                color: new Color([0, 0, 255, 0.5]),
                                width: 2
                            })
                        })
                    });
                    graphicsLayer.add(bufferGraphic);

                    // Query GeoEnrichment service
                    try {
                        const response = await fetch("https://geoenrich.arcgis.com/arcgis/rest/services/World/GeoenrichmentServer/Geoenrichment/enrich", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/x-www-form-urlencoded"
                            },
                            body: new URLSearchParams({
                                f: "json",
                                token: esriConfig.apiKey,
                                studyAreas: JSON.stringify([{
                                    geometry: buffer.toJSON()
                                }]),
                                dataCollections: ["KeyFacts"],
                                returnGeometry: false
                            })
                        });

                        const data = await response.json();
                        results.push({
                            distance: distance,
                            data: data
                        });
                    } catch (error) {
                        console.error("Error querying GeoEnrichment service:", error);
                    }
                }

                // Update info div with results
                let html = "<h3>Buffer Analysis Results</h3>";
                results.forEach(result => {
                    if (result.data && result.data.results && result.data.results[0]) {
                        const keyFacts = result.data.results[0].value.FeatureSet[0].features[0].attributes;
                        html += `<h4>${result.distance}m Buffer</h4>`;
                        html += "<ul>";
                        for (const [key, value] of Object.entries(keyFacts)) {
                            if (key !== "OBJECTID") {
                                html += `<li><strong>${key}:</strong> ${value}</li>`;
                            }
                        }
                        html += "</ul>";
                    }
                });
                infoDiv.innerHTML = html;
            }

            // Listen for point creation in the sketch widget
            sketch.on("create", (event) => {
                if (event.state === "complete" && event.graphic.geometry.type === "point") {
                    analyzePoint(event.graphic.geometry);
                }
            });
        });
    </script>
</head>

<body>
    <div id="viewDiv"></div>
</body>
</html>
```

Let's make some adjustments to make the display more user-friendly.

```text
Move the zoom buttons to the bottom right and make sure the buffer analysis panel is not too long vertically (e.g., 80% of vh) and it's scrollable.
```

And here is the final result:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>UCuenca Map</title>

    <link rel="stylesheet" href="https://js.arcgis.com/4.32/esri/themes/light/main.css">
    <script src="https://js.arcgis.com/4.32/"></script>

    <style>
        html,
        body,
        #viewDiv {
            padding: 0;
            margin: 0;
            height: 100%;
            width: 100%;
        }
        #infoDiv {
            background-color: white;
            padding: 10px;
            width: 300px;
            position: absolute;
            top: 15px;
            left: 15px;
            z-index: 2;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            max-height: 80vh;
            overflow-y: auto;
        }
        .esri-zoom {
            position: absolute;
            bottom: 15px;
            right: 15px;
        }
    </style>

    <script>
        require([
            "esri/Map",
            "esri/views/MapView",
            "esri/config",
            "esri/widgets/Sketch",
            "esri/layers/GraphicsLayer",
            "esri/Graphic",
            "esri/geometry/Point",
            "esri/geometry/Polygon",
            "esri/geometry/geometryEngine",
            "esri/symbols/SimpleFillSymbol",
            "esri/symbols/SimpleLineSymbol",
            "esri/Color",
            "esri/widgets/Zoom"
        ], function(Map, MapView, esriConfig, Sketch, GraphicsLayer, Graphic, Point, Polygon, geometryEngine, SimpleFillSymbol, SimpleLineSymbol, Color, Zoom) {
            // Set the API key
            esriConfig.apiKey = "AAPTxy8BH1VEsoebNVZXo8HurOB-qUDlHkp2KVuV5t-oSPzbtZJWBxFY-pE-rlUKOswgNr30Xf652G73pBqrpNjoWI-KrgkeP4i5jYeq3BczHmj695E-_OZA4Ekk2dyHuLwH6nhi5aui1WZQqHB8Z5q7p0Yx03keZlBiuuNqN32wxbbIv4rs5P0ZBoZamtElNuZrULn8uRnA5Dkvl7XzVkA-B4B9oIU3h-7XRUsADZFgZbQ.AT1_Z9N4skKF";

            // Create a graphics layer for the sketch widget and buffers
            const graphicsLayer = new GraphicsLayer();

            // Create a Map instance
            const map = new Map({
                basemap: "arcgis/navigation",
                layers: [graphicsLayer]
            });

            // Create a MapView instance
            const view = new MapView({
                container: "viewDiv",
                map: map,
                center: [-78.9875, -2.9006], // Coordinates of Universidad de Cuenca
                zoom: 15
            });

            // Create the sketch widget
            const sketch = new Sketch({
                view: view,
                layer: graphicsLayer,
                creationMode: "hybrid"
            });

            // Add the sketch widget to the top right of the view
            view.ui.add(sketch, "top-right");

            // Create and add zoom widget to bottom right
            const zoom = new Zoom({
                view: view
            });
            view.ui.add(zoom, "bottom-right");

            // Create info div
            const infoDiv = document.createElement("div");
            infoDiv.id = "infoDiv";
            infoDiv.innerHTML = "<h3>Buffer Analysis</h3><p>Click a point to see KeyFacts for different buffer zones.</p>";
            view.ui.add(infoDiv, "top-left");

            // Function to create buffer and query GeoEnrichment
            async function analyzePoint(point) {
                const buffers = [500, 1000, 2000]; // Buffer distances in meters
                let results = [];

                // Clear previous graphics
                graphicsLayer.removeAll();

                // Add the clicked point
                const pointGraphic = new Graphic({
                    geometry: point,
                    symbol: {
                        type: "simple-marker",
                        style: "circle",
                        color: "red",
                        size: "8px"
                    }
                });
                graphicsLayer.add(pointGraphic);

                // Create buffers and query for each
                for (const distance of buffers) {
                    // Create buffer
                    const buffer = geometryEngine.buffer(point, distance, "meters");
                    
                    // Create buffer graphic
                    const bufferGraphic = new Graphic({
                        geometry: buffer,
                        symbol: new SimpleFillSymbol({
                            color: new Color([0, 0, 255, 0.1]),
                            outline: new SimpleLineSymbol({
                                color: new Color([0, 0, 255, 0.5]),
                                width: 2
                            })
                        })
                    });
                    graphicsLayer.add(bufferGraphic);

                    // Query GeoEnrichment service
                    try {
                        const response = await fetch("https://geoenrich.arcgis.com/arcgis/rest/services/World/GeoenrichmentServer/Geoenrichment/enrich", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/x-www-form-urlencoded"
                            },
                            body: new URLSearchParams({
                                f: "json",
                                token: esriConfig.apiKey,
                                studyAreas: JSON.stringify([{
                                    geometry: buffer.toJSON()
                                }]),
                                dataCollections: ["KeyFacts"],
                                returnGeometry: false
                            })
                        });

                        const data = await response.json();
                        results.push({
                            distance: distance,
                            data: data
                        });
                    } catch (error) {
                        console.error("Error querying GeoEnrichment service:", error);
                    }
                }

                // Update info div with results
                let html = "<h3>Buffer Analysis Results</h3>";
                results.forEach(result => {
                    if (result.data && result.data.results && result.data.results[0]) {
                        const keyFacts = result.data.results[0].value.FeatureSet[0].features[0].attributes;
                        html += `<h4>${result.distance}m Buffer</h4>`;
                        html += "<ul>";
                        for (const [key, value] of Object.entries(keyFacts)) {
                            if (key !== "OBJECTID") {
                                html += `<li><strong>${key}:</strong> ${value}</li>`;
                            }
                        }
                        html += "</ul>";
                    }
                });
                infoDiv.innerHTML = html;
            }

            // Listen for point creation in the sketch widget
            sketch.on("create", (event) => {
                if (event.state === "complete" && event.graphic.geometry.type === "point") {
                    analyzePoint(event.graphic.geometry);
                }
            });
        });
    </script>
</head>

<body>
    <div id="viewDiv"></div>
</body>
</html>
```

Congratulations! You have just created a web map with a toolbar and a GeoEnrichment service. Now it's yourt turn to be more creative and add more features to the web map.

## 4. Conclusion

In this tutorial, we have learned how to use the ArcGIS API for Python to create a web map with a toolbar and a GeoEnrichment service. We have also learned how to use Cursor to create a web map with a toolbar and a GeoEnrichment service.

We have also learned how to use the ArcGIS API for Python to create a web map with a toolbar and a GeoEnrichment service. We have also learned how to use Cursor to create a web map with a toolbar and a GeoEnrichment service.

We have also learned how to use the ArcGIS API for Python to create a web map with a toolbar and a GeoEnrichment service. We have also learned how to use Cursor to create a web map with a toolbar and a GeoEnrichment service.

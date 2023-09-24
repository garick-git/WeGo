let map;

function createMap(accessToken) {
    mapboxgl.accessToken = accessToken
    map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [-97.754717, 30.22837],
        zoom: 12
    });

    map.on('load', () => {
        map.addSource('vehicles', {
            type: 'geojson',
            data: {
                type: 'FeatureCollection',
                features: []
            }
        });

        // Load vehicle image
        map.loadImage('../static/vehicle.png', (error, image) => {
            if (error) throw error;
            map.addImage('vehicle-icon', image);
        });

        map.addLayer({
            id: 'vehicles',
            type: 'symbol',
            source: 'vehicles',
            layout: {
                'icon-image': 'vehicle-icon',
                'icon-size': 0.1,
                'icon-anchor' : 'center'
            }
        });
    

        // Initialize a popup but keep it closed
        const popup = new mapboxgl.Popup({
            closeButton: false,
            closeOnClick: true
        });

        // On click event for the vehicles layer
        map.on('click', 'vehicles', (e) => {
            // Get the properties of the clicked feature
            const properties = e.features[0].properties;
            console.log("properties: " + properties)

            // Create the content for the popup
            const popupContent = `
                <div>
                    <h4>Vehicle ID: ${properties.id}</h4>
                    <p>Fleet Name: ${properties.fleetName}</p>
                    <p>Vehicle Type: ${properties.vehicleMakeModel}</p>
                    <p>Inventory: ${properties.inventory}</p>
                </div>
            `;

            // Set the popup content and location
            popup.setLngLat(e.lngLat)
                .setHTML(popupContent)
                .addTo(map);
        });

        // Replace 'mouseenter' and 'mouseleave' with 'mousemove' event listener
        map.on('mousemove', (e) => {
            // Query the features at the mouse pointer position
            const features = map.queryRenderedFeatures(e.point, {
                layers: ['vehicles']
            });

            // If a vehicle feature is found, change the cursor to a pointer
            if (features.length) {
                map.getCanvas().style.cursor = 'pointer';
            } else {
                map.getCanvas().style.cursor = '';
            }
        });

        // Fetch vehicle locations and update the map
        const updateVehicleLocations = async () => {
            try {
                const response = await fetch('/populateVehicles');
                const vehicles = await response.json();

                const features = vehicles.map(vehicle => ({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        coordinates: vehicle.currLocation
                    },
                    properties: {
                        id: vehicle._id,
                        fleetName: vehicle.fleetName,
                        vehicleMakeModel: vehicle.vehicleMakeModel,
                        status: vehicle.status
                    }
                }));

                map.getSource('vehicles').setData({
                    type: 'FeatureCollection',
                    features
                });

            } catch (error) {
                console.error('Error fetching vehicle locations:', error);
            }
        };

        // Update vehicle locations every second
        setInterval(updateVehicleLocations, 1000);
    });
}
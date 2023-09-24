//pre:none
//post:creates mapboxGL map that is centered at ST EDWARDS
function createMap() {
    // Define the route coordinates
    var start = [-97.754717, 30.22837];//st eds coordinates
    // Define the map
    map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: start,
        zoom: 12
    });
    return map;
}


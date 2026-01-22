
# Thailand Interactive Map

## Overview
This project is a barebones interactive map of Thailand for visualizing and exploring hospital project locations. It features a responsive SVG map, interactive hotspots, and smooth zoom/pan controls. The codebase is modular, with HTML, JavaScript, and CSS separated for clarity and maintainability.

## Features
- **Responsive SVG Map**: The map (inline SVG in `index.html`) scales to fit any screen size, maintaining clarity on desktop and mobile.
- **Interactive Hotspots**: Clickable points represent hospital projects. Hover or click a hotspot to see a popup with details and an image.
- **Zoom & Pan**: Hold Ctrl (or Cmd on Mac) and use the mouse wheel to zoom in/out, centered on the pointer. Drag to pan the map when zoomed in.
- **Customizable Hotspots**: Add or edit hotspots by modifying the `hotspots` array in `main.js`. Each hotspot has coordinates, a label, description, and image.
- **Modern UI**: Styled with a pale blue color scheme, subtle shadows, and a card-based layout (`styles.css`).
- **No External Dependencies**: Only D3.js is loaded from CDN. All map data and logic are in the project files.

## File Structure
- `index.html`: Main HTML file. Contains the inline SVG map and loads the CSS/JS.
- `main.js`: All map logic, interactivity, and the `hotspots` array. Handles SVG coloring, popup logic, zoom/pan, and search.
- `styles.css`: All styles for the map, popups, tooltips, and layout.
- `rsc/`: Resource folder for images (e.g., hospital photos, logo).
- `geocode.py`: Optional Python script for geocoding addresses to coordinates.

## Usage

### Run Locally
1. Make sure you have Python installed.
2. Start a simple HTTP server in this folder:
   - For Python 3: `python -m http.server`
3. Open your browser and go to: [http://localhost:8000/index.html](http://localhost:8000/index.html)

### Explore the Map
- Click hotspots for more information and images.
- Zoom and pan using Ctrl+Wheel and drag.

### Add or Edit Hotspots
1. Open `main.js` and find the `hotspots` array (near the top).
2. Each hotspot is an object with:
   - `provinceId`: SVG province ID (e.g., `TH-41`)
   - `title`: Name of the hospital/project
   - `description`: Short description
   - `x`, `y`: SVG coordinates (match the map's viewBox)
   - `imageUrl`: Path to an image (relative to `rsc/`)
3. Add, remove, or edit entries as needed. Save and refresh the browser to see changes.

### Extend the Map
- Add more SVG paths to the map in `index.html` for new provinces or regions.
- Enhance the JavaScript for dynamic data, filtering, or API integration.

## Advanced Features
- **Popup Smart Positioning**: Popups reposition to stay visible on screen.
- **Pointer-Centered Zoom**: Zooming is centered on the mouse pointer for intuitive navigation.
- **Responsive Hotspot Scaling**: Hotspot sizes and borders scale with the map and zoom level.
- **Keyboard/Touch Friendly**: Hotspots and map controls work with mouse and touch input.
- **Search**: Search for provinces or hospitals using the search box above the map.

## Limitations
- This is a **barebones version**: no backend, persistent data storage, or analytics.
- Only a subset of provinces and hotspots are included by default. Expand by adding more SVG paths or hotspot entries.

---

## geocode.py (Helper Script)

`geocode.py` is a simple Python script to geocode hospital addresses using OpenStreetMap's Nominatim API. It converts addresses to latitude/longitude and can append results to a local file for use in the map.

- **Usage**: Run `python geocode.py` to geocode predefined address groups. Use `--append` to append results to a local file (default: `coordinates.txt`). Change the output file with `--out <path>`.
- **Note**: This script is optional. By default, it writes simple CSV lines (`lat,lon,label`) to the output file. Edit `geocode.py` if you need a different format.

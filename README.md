

# Thailand Interactive Map

Welcome! This project is a simple, interactive map of Thailand designed to help you explore and visualize hospital project locations. It’s lightweight, easy to use, and everything runs right in your browser—no backend or complicated setup required.

---

## What’s Inside?

- **Responsive SVG Map:** The map (inline SVG in `index.html`) looks sharp on any device, from desktop to mobile.
- **Interactive Hotspots:** Clickable points show hospital projects. Hover or click to see a popup with details and a photo.
- **Zoom & Pan:** Hold Ctrl (or Cmd on Mac) and scroll to zoom in/out, centered on your mouse. Drag to pan when zoomed in.
- **Customizable Hotspots:** Add or edit hotspots easily in `main.js`. Each one has coordinates, a label, description, and image.
- **Modern Look:** Clean, pale blue color scheme with subtle shadows and a card-style layout (see `styles.css`).
- **No Heavy Dependencies:** Only D3.js is loaded from CDN. All map data and logic are in the project files.

## Project Structure

- `index.html` — Main HTML file. Contains the SVG map and loads CSS/JS.
- `main.js` — Handles all map logic, interactivity, and the `hotspots` array.
- `styles.css` — All the styles for the map, popups, tooltips, and layout.
- `rsc/` — Images and resources (hospital photos, logo, etc).
- `geocode.py` — (Optional) Python script for geocoding addresses.

## Getting Started

### Run Locally
1. Make sure you have Python installed.
2. Start a simple HTTP server in this folder:
   - For Python 3: `python -m http.server`
3. Open your browser and go to: [http://localhost:8000/index.html](http://localhost:8000/index.html)

### Explore the Map
- Click on hotspots to see more info and images.
- Zoom and pan using Ctrl+Wheel and drag.

### Add or Edit Hotspots
1. Open `main.js` and look for the `hotspots` array near the top.
2. Each hotspot is an object with:
   - `provinceId`: SVG province ID (e.g., `TH-41`)
   - `title`: Name of the hospital/project
   - `description`: Short description
   - `x`, `y`: SVG coordinates (match the map’s viewBox)
   - `imageUrl`: Path to an image (relative to `rsc/`)
3. Add, remove, or edit entries as you like. Save and refresh your browser to see changes.

### Want to Extend the Map?
- Add more SVG paths in `index.html` for new provinces or regions.
- Enhance the JavaScript for dynamic data, filtering, or API integration. (To be Implemented)

## Cool Features

- **Smart Popups:** Popups always try to stay visible on screen.
- **Pointer-Centered Zoom:** Zooming is centered on your mouse pointer for a natural feel.
- **Hotspot Scaling:** Hotspot sizes and borders scale with the map and zoom level.
- **Keyboard & Touch Friendly:** Works with mouse and touch input.
- **Search:** Quickly find provinces or hospitals using the search box above the map.

## Limitations

- This is a **barebones demo**: there’s no backend, persistent data, or analytics.
- Only a few provinces and hotspots are included by default. You can add more by editing the SVG or the `hotspots` array.

---

## geocode.py (Helper Script)

Want to convert hospital addresses to coordinates? `geocode.py` is a simple Python script that uses OpenStreetMap’s Nominatim API to geocode addresses. It writes results to a local file for use in the map.

- **How to use:** Run `python geocode.py` to geocode the built-in address list. Use `--append` to add results to a file (default: `coordinates.txt`). Change the output file with `--out <path>`.
- **Note:** This script is optional. By default, it writes simple CSV lines (`lat,lon,label`). Edit `geocode.py` if you want a different format.

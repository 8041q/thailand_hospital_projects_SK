# Thailand Interactive Map (Barebones Version)

## Overview
This project provides a barebones interactive map of Thailand, designed for visualizing and exploring hospital project locations. The main interface is a responsive HTML page with an inline SVG map, interactive hotspots, and smooth zoom/pan controls. The map is styled for clarity and ease of use, making it suitable as a foundation for more advanced mapping or data visualization projects.

## Features
- **Responsive SVG Map**: The map scales to fit any screen size, maintaining clarity and usability on both desktop and mobile devices.
- **Interactive Hotspots**: Clickable points (hotspots) are overlaid on the map to represent hospital projects or other locations. Hovering or clicking a hotspot displays a popup with details.
- **Zoom & Pan**: Hold Ctrl (or Cmd on Mac) and use the mouse wheel to zoom in/out, centered on the pointer. Drag to pan the map when zoomed in.
- **Customizable**: Easily add more hotspots or locations by editing the JavaScript section in the HTML file. Each hotspot can have its own label, coordinates, and popup content.
- **Clean, Modern UI**: The map is styled with a pale blue color scheme, subtle shadows, and card-based layout for a professional look.
- **No External Dependencies**: Only D3.js is loaded from CDN; all map data and logic are self-contained in the HTML file.


## Usage

- **Run Locally:**
	- Make sure you have Python installed.
	- Start a simple HTTP server in this folder:
		- For Python 3: `python -m http.server`
	- Open your browser and go to: [http://localhost:8000/index.html](http://localhost:8000/index.html)

- **Explore the Map:**
	- Click hotspots for more information.
	- Zoom and pan using Ctrl+Wheel and drag.

- **Add More Locations:**
	- Edit the `hotspots` array in the JavaScript section of `index.html`.
	- Specify coordinates, labels, and popup content for each new hotspot.

- **Extend the Map:**
	- The SVG and code can be expanded for dynamic data, filtering, or API integration.

## Niche Features
- **Popup Smart Positioning:** Popups automatically reposition if they would go off the edge of the screen, so information is always visible.
- **Pointer-Centered Zoom:** Zooming is centered on the mouse pointer for intuitive navigation.
- **Responsive Hotspot Scaling:** Hotspot sizes and borders scale smoothly with the map, staying visible at any zoom level or screen size.
- **Keyboard/Touch Friendly:** Hotspots and map controls are designed to work with both mouse and touch input.

## Limitations
- This is a **barebones version**: it does not include a backend, persistent data storage, or advanced analytics. It is intended as a starting point for custom mapping projects.
- Only a subset of provinces and hotspots are included by default. You can expand the map by adding more SVG paths or hotspot entries.

---

# geocode.py (Helper Script)

A simple Python script to geocode hospital addresses using OpenStreetMap's Nominatim API. It converts addresses to latitude/longitude and can append results to a local file for use in the map.

- **Usage**: Run `python geocode.py` to geocode predefined address groups. Use `--append` to append results to a local file (default: `coordinates.txt`). Change the output file with `--out <path>`.
- **Note**: This script is an optional helper to automate finding coordinates. By default it writes simple CSV lines (`lat,lon,label`) to the output file; edit `geocode.py` if you need a different format.

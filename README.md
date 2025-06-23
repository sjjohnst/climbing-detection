# Cliff Detection Dashboard for Climbing Development

Welcome! This project is a personal dashboard for detecting potential climbing sites, specifically cliffs, using geospatial data and remote sensing techniques. It combines my passion for climbing with my interest in remote sensing and computer science.

## Project Goals

- Detect cliffs and potential climbing areas from DTM (Digital Terrain Model) data.
- Visualize detected features on an interactive map with both polygons/lines and point markers.
- Provide analytics such as cliff height (with uncertainty), orientation, and other relevant statistics.
- Export results as GeoJSON (for spatial data) and CSV (for tabular summaries).
- Learn and implement geospatial data handling, tiling/chunking, and visualization techniques in Python.

## Key Features

- **Offline Processing:** Process large DTM datasets locally, with a focus on simplicity and learning.
- **Tiling/Chunking:** Work with tiled raster data for efficient processing and visualization.
- **Python-Based Visualization:** Use Python tools, specifically Dash, for interactive map displays and analytics.
- **Analytics:** Calculate and display cliff height (with uncertainty based on DTM resolution), orientation, and other statistics.
- **Export Options:** GeoJSON for spatial features, CSV for summaries.

## Data

- Input: DTM .tif files (organized in .zip archives, each ~3GB, with varying file sizes and shapes).
- Output: GeoJSON (polygons/lines, points), CSV (statistics).

## Roadmap

1. **Project Setup**
    - Organize project directory and set up Python environment (using mamba).
    - Gather and inspect DTM data files.

2. **Data Handling**
    - Implement tiling/chunking for efficient raster data processing.
    - Develop utilities for reading and managing tiled .tif files.

3. **Cliff Detection Algorithm**
    - Research and implement feature detection methods for identifying cliffs.
    - Calculate cliff height (with uncertainty based on DTM resolution).
    - Determine cliff orientation (general sun angle/aspect).

4. **Visualization**
    - Build an interactive dashboard using Dash.
    - Display detected cliffs as polygons/lines and point markers.
    - Enable navigation between markers and detailed polygon views.

5. **Analytics & Export**
    - Summarize detected features with statistics (height, orientation, etc.).
    - Export results as GeoJSON (spatial features) and CSV (tabular summaries).

6. **Documentation & Learning**
    - Document code, workflow, and learning outcomes.
    - Explore opportunities for integrating new data sources or advanced features in the future.

---

*This project is for personal learning and development. Contributions and suggestions are welcome!*

## Environment Setup

To create your environment using mamba:

```sh
mamba create -n climbing_detection python=3.11
mamba activate climbing_detection
mamba install --file requirements.txt
```

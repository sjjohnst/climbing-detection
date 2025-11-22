# Project Stack Description

## Overview
This document outlines the technology stack and architecture for the web application designed to display high-resolution DTM (Digital Terrain Model) data interactively. The application consists of a backend for data processing and serving, and a frontend for visualization.

---

## Technology Stack

### **Frontend**
- **Framework**: [React](https://reactjs.org/)  
  A modern, component-based JavaScript library for building interactive user interfaces.
- **Map Library**: [Leaflet](https://leafletjs.com/)  
  A lightweight and easy-to-use library for rendering interactive maps.
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)  
  A utility-first CSS framework for rapid UI development.
- **Build Tool**: [Vite](https://vitejs.dev/)  
  A fast development server and build tool optimized for modern web applications.

---

### **Backend**
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)  
  A Python web framework for building REST APIs, known for its speed and simplicity.
- **Data Processing**: [rioxarray](https://corteva.github.io/rioxarray/stable/) and [NumPy](https://numpy.org/)  
  Libraries for handling raster data and numerical computations.
- **Image Serving**: FastAPI serves preprocessed PNG overlays of the DTM data.
- **Database**: [PostgreSQL](https://www.postgresql.org/) with [PostGIS](https://postgis.net/) (optional)  
  For spatial queries and metadata storage, if needed.

---

### **Interactive Map Tiles**
- **Tiling Tool**: [GDAL](https://gdal.org/) or [Tippecanoe](https://github.com/mapbox/tippecanoe)  
  Tools for preprocessing large DTM files into smaller tiles for efficient rendering.
- **Tile Server**: [TileServer GL](https://tileserver.readthedocs.io/) or serve tiles directly from the backend.

---

### **Deployment**
- **Frontend Hosting**: [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/)  
  Platforms for hosting React applications.
- **Backend Hosting**: [AWS](https://aws.amazon.com/), [Azure](https://azure.microsoft.com/), or [DigitalOcean](https://www.digitalocean.com/)  
  Cloud platforms for hosting the FastAPI backend.
- **Containerization**: [Docker](https://www.docker.com/)  
  Ensures consistent environments for development and deployment.

---

## Software Architecture

### **Frontend**
- React app with Leaflet for map rendering.
- Fetches DTM metadata (bounds, center, etc.) and overlay images from the backend via REST API.
- Displays the DTM as an interactive map layer.

### **Backend**
- **DTM Preprocessing**:
  - On startup, preprocesses the DTM file into smaller tiles or a single PNG overlay.
  - Caches the processed data in memory or on disk for fast access.
- **API Endpoints**:
  - `/dtm_info`: Serves metadata about the DTM (bounds, center, etc.).
  - `/dtm.png`: Serves the preprocessed PNG overlay.
  - `/tiles/{z}/{x}/{y}.png`: Serves map tiles (if tiling is implemented).
  - `/dtm_debug`: Provides debugging information about the DTM file.
- **Error Handling**:
  - Handles cases where the DTM file is missing or corrupted.
  - Provides meaningful error messages to the frontend.

---

## Data Flow
1. Backend preprocesses the DTM file into a format suitable for web display (e.g., PNG overlay or tiles).
2. Frontend fetches metadata and overlay/tiles from the backend.
3. Frontend renders the map using Leaflet, overlaying the DTM data.

---

## Next Steps
1. **Backend Enhancements**:
   - Update the backend to support tiling (if needed) and optimize the preprocessing pipeline.
   - Add endpoints for serving tiles or overlays.

2. **Frontend Development**:
   - Set up a React project with Leaflet and Tailwind CSS.
   - Create a basic map interface that fetches and displays the DTM overlay.

3. **Data Preprocessing**:
   - Use GDAL to preprocess the `laurentides_dtm.tif` file into tiles or a downsampled overlay.

4. **Deployment**:
   - Set up Docker for containerized development.
   - Deploy the backend and frontend to a
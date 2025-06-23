# Project Notes

## Progress Log

### 2025-06-23

#### What’s working:
- Automated extraction of `.tif` files from `.zip` archives to `data/extracted/`
- Inspection of `.tif` metadata and masking of NoData values (nodata = -32767)
- Visualization of DEM and slope using masked arrays (color scaling now correct)
- Slope calculation and display for initial cliff detection prototyping

#### Key decisions:
- Use 2000x2000 pixel tiles as processing units (no further chunking for now)
- No overlap between tiles at this stage; revisit if edge effects are observed
- Mask NoData values using the raster’s nodata metadata (currently -32767)
- File size differences between tiles are normal (compression, data content)
- If detection at tile edges is problematic, consider implementing overlap

---

## TODO

- [ ] Prototype and refine cliff detection logic (e.g., thresholding slope)
- [ ] Add unit tests for detection and masking
- [ ] Consider batch processing of all tiles
- [ ] Plan for exporting detected features (GeoJSON, CSV)
- [ ] Investigate and document the CRS and metadata for all tiles
- [ ] Save example output plots for quick verification
- [ ] Review and update documentation as new insights are gained

---

*Add new notes and progress updates here as you continue development.*
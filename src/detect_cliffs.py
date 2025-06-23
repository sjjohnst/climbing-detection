import os
import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from scipy import ndimage

def compute_slope(dem, pixel_size):
    """
    Compute the slope (in degrees) of a DEM using Sobel filters.

    Parameters:
        dem (np.ndarray): 2D array of elevation values.
        pixel_size (float): Spatial resolution of each pixel (assumes square pixels).

    Returns:
        np.ndarray: 2D array of slope values in degrees.
    """
    # Calculate gradient in x and y directions using Sobel operator
    dx = ndimage.sobel(dem, axis=1) / (8 * pixel_size)
    dy = ndimage.sobel(dem, axis=0) / (8 * pixel_size)
    # Compute slope in degrees
    slope = np.arctan(np.hypot(dx, dy)) * (180 / np.pi)
    return slope

def main():
    """
    Loads the first .tif DEM file from the extracted data directory,
    masks NoData values, computes the slope, and visualizes both the DEM and slope.
    """
    # Directory containing extracted .tif files
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'extracted')
    # List all .tif files in the directory
    tif_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.tif')]
    if not tif_files:
        print("No .tif files found in extracted directory.")
        return

    # Use the first .tif file for demonstration
    tif_path = os.path.join(data_dir, tif_files[0])
    with rasterio.open(tif_path) as src:
        dem = src.read(1)  # Read the first band (assumed to be elevation)
        pixel_size = src.res[0]  # Pixel size (assumes square pixels)
        nodata = src.nodata      # NoData value from metadata

    # Mask NoData values for accurate analysis and visualization
    if nodata is not None:
        print("Using nodata value for masking:", nodata)
        dem_masked = np.ma.masked_equal(dem, nodata)
    else:
        # Fallback: mask extreme negative values (common in DEMs)
        print("No nodata value found, masking -9999 as NoData.")
        dem_masked = np.ma.masked_less_equal(dem, -9999)

    # Compute slope using the masked DEM
    slope = compute_slope(dem, pixel_size)
    # Apply the same mask to the slope array
    slope_masked = np.ma.masked_array(slope, mask=dem_masked.mask)  # pylint: disable=no-member

    # Visualize DEM and slope side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.set_title("DEM (masked)")
    show(dem_masked, ax=ax1, cmap='terrain')
    ax2.set_title("Slope (degrees, masked)")
    show(slope_masked, ax=ax2, cmap='inferno')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

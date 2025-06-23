import os
import rasterio

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def list_tif_files(data_dir):
    """
    Generator that yields full paths to all .tif files in the given directory and its subdirectories.

    Parameters:
        data_dir (str): Path to the directory to search for .tif files.

    Yields:
        str: Full path to a .tif file.
    """
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.lower().endswith('.tif'):
                yield os.path.join(root, file)

def print_metadata(tif_path):
    """
    Prints metadata for a given .tif file, including CRS, shape, resolution, and bounds.

    Parameters:
        tif_path (str): Full path to the .tif file.
    """
    with rasterio.open(tif_path) as src:
        print(f"File: {os.path.basename(tif_path)}")
        print(f"  CRS: {src.crs}")
        print(f"  Shape: {src.width} x {src.height}")
        print(f"  Resolution: {src.res}")
        print(f"  Bounds: {src.bounds}")
        print("-" * 40)

if __name__ == "__main__":
    # Iterate through all .tif files in the data directory and print their metadata
    for tif_file in list_tif_files(DATA_DIR):
        print_metadata(tif_file)

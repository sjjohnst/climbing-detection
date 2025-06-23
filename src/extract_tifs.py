import os
import zipfile

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
EXTRACT_DIR = os.path.join(DATA_DIR, 'extracted')

def list_zip_files(data_dir):
    """
    Returns a list of all .zip files in the specified directory.

    Parameters:
        data_dir (str): Path to the directory to search for .zip files.

    Returns:
        list of str: List of full paths to .zip files.
    """
    return [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.lower().endswith('.zip')]

def list_tifs_in_zip(zip_path):
    """
    Lists all .tif files contained within a .zip archive.

    Parameters:
        zip_path (str): Path to the .zip archive.

    Returns:
        list of str: List of .tif file names inside the archive.
    """
    with zipfile.ZipFile(zip_path, 'r') as z:
        return [f for f in z.namelist() if f.lower().endswith('.tif')]

def extract_tifs(zip_path, tif_names, extract_dir):
    """
    Extracts specified .tif files from a .zip archive to a target directory.

    Parameters:
        zip_path (str): Path to the .zip archive.
        tif_names (list of str): List of .tif file names to extract.
        extract_dir (str): Directory to extract files into.
    """
    with zipfile.ZipFile(zip_path, 'r') as z:
        for tif in tif_names:
            print(f"Extracting {tif} from {os.path.basename(zip_path)}")
            z.extract(tif, path=extract_dir)

if __name__ == "__main__":
    # Ensure the extraction directory exists
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    # Find all zip files in the data directory
    zip_files = list_zip_files(DATA_DIR)
    for zip_file in zip_files:
        # List all .tif files in the current zip
        tifs = list_tifs_in_zip(zip_file)
        print(f"{os.path.basename(zip_file)} contains {len(tifs)} .tif files.")
        # Example: extract the first 2 .tif files from each zip for testing
        subset = tifs[:2]
        extract_tifs(zip_file, subset, EXTRACT_DIR)

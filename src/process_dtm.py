import argparse
import os
from pathlib import Path
import numpy as np
import rasterio

def compute_slope(dtm_arr, res_x, res_y):
    dz_dx, dz_dy = np.gradient(dtm_arr, res_y, res_x)
    slope = np.sqrt(dz_dx**2 + dz_dy**2)
    slope_deg = np.degrees(np.arctan(slope))
    return slope_deg

def main(args):
    src = Path(args.input)
    out_dir = Path(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    with rasterio.open(src) as src_ds:
        dtm_arr = src_ds.read(1).astype(np.float32)
        dtm_arr[dtm_arr == src_ds.nodata] = np.nan
        res_x, res_y = src_ds.res[0], src_ds.res[1]
        profile = src_ds.profile

    slope_deg = compute_slope(dtm_arr, res_x, res_y)
    profile.update(dtype=rasterio.float32, count=1, nodata=np.nan)

    original_name = src.stem
    slope_path = out_dir / f"{original_name}_slope.tif"
    with rasterio.open(slope_path, 'w', **profile) as dst:
        dst.write(slope_deg.astype(np.float32), 1)

    print("Slope saved:", slope_path)
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="input DTM GeoTIFF")
    p.add_argument("--out-dir", default="./processed", help="output directory")
    args = p.parse_args()
    main(args)
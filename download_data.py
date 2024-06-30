#!/usr/bin/env python
# coding: utf-8
import requests
import pandas as pd
import os

def download_geo_data(geo_id, output_path):
    url = f"https://ftp.ncbi.nlm.nih.gov/geo/series/{geo_id[:-3]}nnn/{geo_id}/matrix/{geo_id}_series_matrix.txt.gz"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"{output_path}/{geo_id}_series_matrix.txt.gz", 'wb') as f:
            f.write(response.content)
        print(f"Data downloaded and saved to {output_path}")
    else:
        print("Failed to download data")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Download GEO data.")
    parser.add_argument("geo_id", type=str, help="The GEO Series ID.")
    parser.add_argument("output_path", type=str, help="The local path where the data will be saved.")
    args = parser.parse_args()
    os.makedirs(args.output_path, exist_ok=True)
    download_geo_data(args.geo_id, args.output_path)
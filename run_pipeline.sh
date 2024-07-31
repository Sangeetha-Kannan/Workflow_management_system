#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <geo_id> <output_path> <visualization_path>"
    exit 1
fi

GEO_ID=$1
OUTPUT_PATH=$2
VISUALIZATION_PATH=$3

# Create output directory if it does not exist
mkdir -p $OUTPUT_PATH
mkdir -p $VISUALIZATION_PATH

# Step 1: Download the data
python download_data.py $GEO_ID $OUTPUT_PATH

# Step 2: Process the data
python process_data.py ${OUTPUT_PATH}/${GEO_ID}_series_matrix.txt.gz $OUTPUT_PATH

# Step 3: Visualize the data
python visualize_data.py ${OUTPUT_PATH}/average_expression.csv $VISUALIZATION_PATH

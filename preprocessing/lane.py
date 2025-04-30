import os
import pandas as pd
from shapely.geometry import Point, Polygon
import argparse
import json

# 1. Convert RoI data into Polygons
def create_roi_polygons(roi_data):
    roi_polygons = {}
    for site, sections in roi_data.items():
        roi_polygons[site] = {}
        for section, lanes in sections.items():
            roi_polygons[site][section] = {
                lane: Polygon(coords) for lane, coords in lanes.items()
            }
    return roi_polygons

# 2. Assign lanes to vehicle data by comparing with RoI
def assign_lanes(vehicle_data, roi_polygons, site_name):
    assigned_data = []

    for _, row in vehicle_data.iterrows():
        point = Point(row['center_x'], row['center_y'])
        lane_assigned = None

        if site_name in roi_polygons:
            for section, lanes in roi_polygons[site_name].items():
                for lane, polygon in lanes.items():
                    if polygon.contains(point):
                        lane_assigned = f"{section}{lane}"
                        assigned_data.append({**row, 'site': site_name, 'lane': lane_assigned})
                        break
                if lane_assigned:
                    break

        if not lane_assigned:
            continue

    return pd.DataFrame(assigned_data)

# 3. Main Code
def main(site, input_directory, output_directory, roi_json_path):
    with open(roi_json_path, "r") as f:
        roi_data = json.load(f)

    site_name = f"Site {site}"

    roi_polygons = create_roi_polygons(roi_data)

    # Process all CSV files in the input directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(input_directory):
        if file_name.endswith(".csv"):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_path = os.path.join(output_directory, file_name)

            vehicle_data = pd.read_csv(input_file_path)

            assigned_data = assign_lanes(vehicle_data, roi_polygons, site_name)

            assigned_data.to_csv(output_file_path, index=False)
            print(f"Processing complete: {input_file_path} -> {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assign lanes to vehicle data based on RoI")

    parser.add_argument(
        "--site", 
        type=str, 
        required=True, 
        help="Site name for processing"
    )
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="Path to input CSV directory"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        required=True, 
        help="Path to output CSV directory"
    )
    parser.add_argument(
        "--roi", 
        type=str, 
        required=True, 
        help="Path to RoI JSON file"
    )

    args = parser.parse_args()

    main(args.site, args.input, args.output, args.roi)

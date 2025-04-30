import json
import pandas as pd
import os
import argparse

def main(json_dir_path, output_dir):
    json_file_paths = [
        os.path.join(json_dir_path, file) for file in os.listdir(json_dir_path) if file.endswith('.json')
    ]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for json_file_path in json_file_paths:
        json_file_name = os.path.basename(json_file_path)
        output_csv_path = os.path.join(output_dir, json_file_name.replace('.json', '.csv'))

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        rows = []
        for entry in data:
            frame = entry['frame']
            for obj in entry['obb']:
                rows.append({
                    "track_id": obj['track_id'],
                    "frame": frame,
                    "center_x": obj['center'][0],
                    "center_y": obj['center'][1],
                    "width": obj['dimensions'][0],
                    "height": obj['dimensions'][1],
                    "angle": obj['angle'],
                    "x1": obj['polygon'][0],
                    "y1": obj['polygon'][1],
                    "x2": obj['polygon'][2],
                    "y2": obj['polygon'][3],
                    "x3": obj['polygon'][4],
                    "y3": obj['polygon'][5],
                    "x4": obj['polygon'][6],
                    "y4": obj['polygon'][7],
                    "confidence": obj['confidence'],
                    "class_id": obj['class_id']
                })

        df = pd.DataFrame(rows)
        df = df.sort_values(by=['track_id', 'frame'])

        df.to_csv(output_csv_path, index=False)

        print(f"CSV file has been saved: {output_csv_path}")

    print("All JSON files have been processed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")

    parser.add_argument(
        "--json_dir", 
        type=str, 
        required=True, 
        help="Path to directory containing JSON files"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        required=True, 
        help="Path to directory to save CSV files"
    )

    args = parser.parse_args()
    main(args.json_dir, args.output)

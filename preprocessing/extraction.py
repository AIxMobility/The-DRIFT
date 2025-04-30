import subprocess
import os

def run_command(command: str):
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def main():
    # Setting
    model_path = './model/YOLO11OBBm.pt'
    input_video = './data/sample_video/DJI_0025_cut1_stab.mp4'
    output_json_dir = './data/output/test_json'
    output_csv_dir = './data/output/test_csv'
    processed_csv_dir = './data/output/processed_csv'
    roi_path = './preprocessing/roi.json'
    site_code = 'B'

    # 1. trajectory extraction
    run_command(
        f"python3 preprocessing/detect_and_track.py "
        f"--model '{model_path}' "
        f"--input '{input_video}' "
        f"--output '{output_json_dir}'"
    )

    # 2. json to csv
    run_command(
        f"python3 preprocessing/json_to_csv.py "
        f"--json_dir '{output_json_dir}' "
        f"--output '{output_csv_dir}'"
    )

    # 3. add lane variable
    run_command(
        f"python3 preprocessing/lane.py "
        f"--site '{site_code}' "
        f"--input '{output_csv_dir}' "
        f"--output '{processed_csv_dir}' "
        f"--roi '{roi_path}'"
    )

if __name__ == "__main__":
    main()

# trajectory extraction
python3 preprocessing/detect_and_track.py \
    --model './model/YOLO11OBBm.pt' \
    --input './data/sample_video/DJI_0025_cut1_stab.mp4' \
    --output './data/output/test_json'

# json to csv
python3 preprocessing/json_to_csv.py \
    --json_dir './data/output/test_json' \
    --output './data/output/test_csv'

# add lane variable
python3 preprocessing/lane.py \
    --site "B" \
    --input "./data/output/test_csv" \
    --output "./data/output/processed_csv" \
    --roi "./preprocessing/roi.json"

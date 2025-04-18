# trajectory extraction
python detect_and_track.py \
    --model './model/YOLO11OBBm.pt' \
    --input './data/sample_video/DJI_0008_cut_stab.mp4' \
    --output './data/output/test_json'

# json to csv
python json_to_csv.py \
    --json_dir './data/output/test_json' \
    --output './data/output/test_csv'

# add lane variable
python lane.py \
    --site "B" \
    --input "./data/output/test_csv" \
    --output "./data/output/processed_csv" \
    --roi "./extraction/preprocessing/roi.json"

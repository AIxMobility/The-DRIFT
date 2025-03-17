# 🗂️ Additinal Files
- `detect_and_track.py` : Python script to implement object detection and tracking for the DRIFT dataset. The script detects traffic objects (e.g. cars, buses, trucks) in pre-processed drone video frames, generates vehicle trajectories, applies orientation bounding boxes (OBBs) to accurately capture vehicle orientation, and provides data in the form of a json file for subsequent traffic analysis.
 
- `json_to_csv.py` : Python script designed to convert traffic data in JSON format extracted from drone footage to CSV format. The script processes structured data (e.g. vehicle coordinates, IDs, attributes) during the preprocessing and detection stages so that it can be seamlessly integrated into the final CSV-based dataset available on GitHub, and supports flexible format conversions such as JSON.           

- `lane.py` : Python script to easily set up lane-specific regions of interest (RoI) in the preprocessing pipeline for DRIFT datasets. The script assigns unique codes to individual lanes within the stabilised drone footage and defines the lane-specific RoI in polygonal format.
 
- `roi.json` : A json file containing the roi for each site-specific lane, used by `lane.py`.

- `run.sh` : Defined to run all of the preprocessing, and can be commented out as needed to run only the necessary files. 

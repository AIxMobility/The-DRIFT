# 🗂️ Additinal Files
- `detect_and_track.py` : Python script to implement object detection and tracking for the DRIFT dataset. The script detects traffic objects (e.g. cars, buses, trucks) in pre-processed drone video frames, generates vehicle trajectories, applies orientation bounding boxes (OBBs) to accurately capture vehicle orientation, and provides data in the form of a json file for subsequent traffic analysis.
 
- `json_to_csv.py` : Python script designed to convert traffic data in JSON format extracted from drone footage to CSV format. The script processes structured data (e.g. vehicle coordinates, IDs, attributes) during the preprocessing and detection stages so that it can be seamlessly integrated into the final CSV-based dataset available on GitHub, and supports flexible format conversions such as JSON.           

- `lane.py` : Python script to easily set up lane-specific regions of interest (RoI) in the preprocessing pipeline for DRIFT datasets. The script assigns unique codes to individual lanes within the stabilised drone footage and defines the lane-specific RoI in polygonal format.
 
- `roi.json` : A json file containing the roi for each site-specific lane, used by `lane.py`.

- `run.sh` : Defined to run all of the preprocessing, and can be commented out as needed to run only the necessary files. 


## Commands Used
1. Run all processes at once :
- Set the output of `detect_and_track.py` and the input of `json_to_csv.py` to be the same
- Set the output of `json_to_csv.py` and the input of `lane.py` to be the same
```python
sh run.sh
```

2. Run only `detect_and_track.py` : Choose between two methods
```python
python detect_and_track.py
 --model <Your Model Path> \
 --input <Input Video Path> \
 --output <Output Path>
```
```python
# After commenting out lines 7 to 17
sh run.sh
```
  
3. Run only `json_to_csv.py` : Choose between two methods
```python
python json_to_csv.py
 --json_dir <Your Json File Path> \
 --output <Output Path>
```
```python
# After commenting out lines 1 to 5 and 12 to 17
sh run.sh
```
      
4. Run only `lane.py` : Choose between two methods
```python
python lane.py
 --site <Site corresponding to the dataset> \
 --input <CSV File Path> \
 --output <Output Path> \
 --roi <Path to the Json file containing the ROI information>
```
```python
# After commenting out lines 1 to 10
sh run.sh
``` 

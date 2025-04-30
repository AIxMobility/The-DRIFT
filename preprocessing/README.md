# preprocessing

## stabilo
- **`stabilization.sh`**,**`stabilization.py`** : This script is used to stabilize a given video using a reference frame. It sets necessary environment variables and executes the stabilization script with the specified options.

### Commands Used

1. Run the stabilization script
This command will run the stabilization process for the given video using the reference frame.
```bash
sh stabilization.sh
```

2. Explanation of Parameters
The **`stabilization.sh`** script uses the following parameters:

- **`VIDEO_PATHS`**: Video paths to stabilize
- **`REF_FRAME_PATH`**: Path to the reference frame of the video to be stabilized.
- **`SCRIPT_PATH`**: Path to the file to be executed.
- **`OPTIONS`**: Enable or disable saving the stabilized video output and masking, **`default`** : --save, --no-mask

### Acknowledgement

This project is based on the [Stabilo](https://github.com/rfonod/stabilo) repository by Robert Fonod, licensed under the MIT License.  
Certain parts have been adapted and modified to better suit the needs of this project.
- `GitHub` : [https://github.com/rfonod/stabilo](https://github.com/rfonod/stabilo)
```
@software{fonod2025stabilo,
  author = {Fonod, Robert},
  license = {MIT},
  month = apr,
  title = {Stabilo: A Comprehensive Python Library for Video and Trajectory Stabilization with User-Defined Masks},
  url = {https://github.com/rfonod/stabilo},
  doi = {10.5281/zenodo.12117092},
  version = {1.0.1},
  year = {2025}
}
```  
- `DOI` : [10.5281/zenodo.12117092](https://doi.org/10.5281/zenodo.12117092)
```
@misc{fonod2025advanced,
  title={Advanced computer vision for extracting georeferenced vehicle trajectories from drone imagery}, 
  author={Robert Fonod and Haechan Cho and Hwasoo Yeo and Nikolas Geroliminis},
  year={2025},
  eprint={2411.02136},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2411.02136},
  doi={https://doi.org/10.48550/arXiv.2411.02136}
}
```

## extraction
- **`detect_and_track.py`** : Python script to implement object detection and tracking for the DRIFT dataset. The script detects traffic objects (e.g. cars, buses, trucks) in pre-processed drone video frames, generates vehicle trajectories, applies orientation bounding boxes (OBBs) to accurately capture vehicle orientation, and provides data in the form of a json file for subsequent traffic analysis.
 
- **`json_to_csv.py`** : Python script designed to convert traffic data in JSON format extracted from drone footage to CSV format. The script processes structured data (e.g. vehicle coordinates, IDs, attributes) during the preprocessing and detection stages so that it can be seamlessly integrated into the final CSV-based dataset available on GitHub, and supports flexible format conversions such as JSON.           

- **`lane.py`** : Python script to easily set up lane-specific regions of interest (RoI) in the preprocessing pipeline for DRIFT datasets. The script assigns unique codes to individual lanes within the stabilised drone footage and defines the lane-specific RoI in polygonal format.
 
- **`roi.json`** : A json file containing the roi for each site-specific lane, used by **`lane.py`**.

- **`extraction.sh`**,**`extraction.py`**  : Defined to run all of the preprocessing, and can be commented out as needed to run only the necessary files.
  
### Commands Used
1. Run the extraction script :
- Set the output of **`detect_and_track.py`** and the input of **`json_to_csv.py`** to be the same
- Set the output of **`json_to_csv.py`** and the input of **`lane.py`** to be the same
```python
sh extraction.sh
```

2. Explanation of Parameters
The **`extraction.sh`** script uses the following parameters:

- **`trajectory extraction`**
  - **`--model`** : Your model path
  - **`--input`** : Input video path
  - **`--output`** : Output path

- **`json to csv`**
  - **`--json_dir`** : Your json file path
  - **`--output`** : Output path

- **`add lane variable`**
  - **`--site`** : Site corresponding to the dataset
  - **`--input`** : CSV file path
  - **`--output`** : Output path
  - **`--roi`** : Path to the json file containing the ROI information

## geoalign

- **`geoalign_roi.json`** : Includes normal point-in-time roi (Site_F / Site_G) and abnormal point-in-time roi (Site_F_raw / Site_G_raw) for Site F/G
 
- **`geoalign_transformation.ipynb`** : A file for frame alignment, which aligns the ROI of an abnormal viewpoint with the ROI of a normal viewpoint.           

![Image](https://github.com/user-attachments/assets/679338a4-b24b-49ca-87d1-825c0fefa453)




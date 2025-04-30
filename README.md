# The DRIFT Open Dataset

## Overview
**DRIFT (Drone-derived Intelligent for Traffic analysis)** is an open-source dataset designed to support advanced traffic behavior research using high-resolution drone imagery. It enables accurate vehicle detection, trajectory tracking, and traffic flow analysis across complex urban intersections.

## Objectives
- Provide a large-scale, annotated drone dataset optimized for traffic analysis
- Support urban mobility research with pre-trained models and analytical tools
- Enable multi-scale traffic analysis (microscopic, mesoscopic, and macroscopic)

## Contributions
- o detect and track vehicle instances in high resolution using polygon-based oriented bounding boxes (OBB) at an **altitude of 250 meters**
- To stabilize video data and real-world orthophoto-mapped trajectories
- To provide **81,699 annotated vehicle trajectories** collected across 2.6 km of urban roadways
- To offer object detection/tracking model for customization and the built-in tools for lane-change analysis, time-to-collision (TTC), congestion detection, flow-density analysis, and more
  
## Dataset Specifications![ttc_new]

- **Site coverage**: 9 interconnected urban intersections in Daejeon, South Korea
  - Target site: From 99 Daehak-ro to 291 Daehak-ro Daejeon in South Korea <img width="1479" alt="Image" src="https://github.com/user-attachments/assets/788bb716-c24d-4910-b10d-b724af3e8f0d" />
- **Imagery**: 4K drone footage with frame-level annotations  
- **Trajectory format**: Real-world coordinates with speed, acceleration, and heading  
- **Model**: YOLOv11m + ByteTrack with polygon-based OBB detection

## Demos
- Frame stabilization
<video src="https://github.com/user-attachments/assets/3468c496-dd18-445f-ab59-324beb871037" controls width="600">
  Your browser does not support the video tag.
</video>
- Result of object detection using YOLOv11m model (approximately 300K vehicle instances manually annotated)
<video src="https://github.com/user-attachments/assets/08aed82e-8514-4fd8-bb57-b651b7e30ff6" controls width="600">
  Your browser does not support the video tag.
</video>
- Visualized trajectories in DRIFT open dataset
<img src="https://github.com/user-attachments/assets/8c270a64-e8c1-46f5-95b9-026bcc0dd40b" width="70%"/>

## Download Dataset (Huggingface)
https://huggingface.co/datasets/Hj-Lee/The-DRIFT

## Download Dataset (in Python)
```
# DRIFT dataset load
from datasets import load_dataset

dataset = load_dataset("Hj-Lee/The-DRIFT")
```
## Model Customization 
```bash
# Clone the repository
git clone https://github.com/AIxMobility/The-DRIFT

# Create conda env
conda create -n DRIFT python=3.11 -y

# Install dependencies
pip install -r requirements.txt

# Preprocess the dataset
sh preprocessing/extraction.sh
python preprocessing/extraction.py

# Stabilize drone video
sh preprocessing/stabilization.sh
python preprocessing/stabilization.py

# Train detection model
python model/train.py
```

## Repository Structure

```DroneTrack/
│
├── data/                      # Raw and processed drone data
│   ├── csv/                   # Frame-level trajectory metadata
│   ├── sample_video/          # Sample drone videos
│   ├── site_images/           # Reference frames in each site
│
├── preprocessing/                # Data extraction and stabilization
│   ├── detect_and_track.py
│   ├── json_to_csv.py             
│   ├── lane.py
│   ├── RoI.json
│   ├── extraction.sh
│   ├── extraction.py
│   ├── stabilo               # Stabilization scripts (Ack.: https://github.com/rfonod/stabilo)
│   ├── scripts
│   ├── stabilization.sh
│   ├── stabilization.py
│   ├── geoalign_roi.json
│   ├── geoalign_transformation.ipynb
|
├── model/                     # Annotation data and model training
│   ├── test/                   
│   ├── train/           
│   ├── valid/
│   ├── data.yaml                   
│   ├── drone_data.yaml           
│   ├── train.py
│   ├── best.pt
|
├── utils/                     # Utility scripts for data handling
│   ├── convert.py
│   ├── video_to_frame.py
│
├── vis/                       # Visualization scripts and tools
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── performance_analysis.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE

```

## Visualizations of Traffic Analysis Tools
<table>
  <thead>
    <tr>
      <th>Scale</th>
      <th>Description</th>
      <th>Image</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><b>Microscopic</b></td>
      <td>Lane Change (LC)</td>
      <td><img src="https://github.com/user-attachments/assets/e5146f82-9ab4-4e4c-ac83-30dbcb537e25" width="70%"/></td>
    </tr>
    <tr>
      <td>Time-to-Collision (TTC)</td>
      <td><img src="https://github.com/user-attachments/assets/578cdc8a-e2cb-4613-9953-6e7890177251" width="70%"/></td>
    </tr>
    <tr>
      <td rowspan="2"><b>Mesoscopic</b></td>
      <td>Flow-Density Diagram </td>
      <td><img src="https://github.com/user-attachments/assets/473d7545-c73c-4fd1-bc92-e818f64f872f" width="70%"/></td>
    </tr>
    <tr>
      <td>Time-Space Diagram </td>
      <td><img src="https://github.com/user-attachments/assets/914bcdd2-2bac-4d34-95f9-9f38852a93fe" width="70%"/></td>
    </tr>
    <tr>
      <td><b>Macroscopic</b></td>
      <td>Speed Heatmap</td>
      <td><img src="https://github.com/user-attachments/assets/b08961ca-cf78-428c-9540-7bd173cdf577" width="70%"/></td>
    </tr>
  </tbody>
</table>

## Acknowledgement

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


## Citation
If you use this project in your academic research, commercial products, or any published material, please acknowledge its use by citing it.
```
@misc{lee2025driftopendatasetdronederived,
      title={DRIFT open dataset: A drone-derived intelligence for traffic analysis in urban environment}, 
      author={Hyejin Lee and Seokjun Hong and Jeonghoon Song and Haechan Cho and Zhixiong Jin and Byeonghun Kim and Joobin Jin and Jaegyun Im and Byeongjoon Noh and Hwasoo Yeo},
      year={2025},
      eprint={2504.11019},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.11019}, 
}
```


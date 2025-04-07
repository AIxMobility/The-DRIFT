# The DRIFT Open Dataset

## Overview
**DRIFT (Drone-derived Intelligent for Traffic analysis)** is an open-source dataset designed to support advanced traffic behavior research using high-resolution drone imagery. It enables accurate vehicle detection, trajectory tracking, and traffic flow analysis across complex urban intersections.

## Objectives
- Provide a large-scale, annotated drone dataset optimized for traffic analysis
- Support urban mobility research with pre-trained models and analytical tools
- Enable multi-scale traffic analysis (microscopic, mesoscopic, and macroscopic)

## Contributions
- 81,699 annotated vehicle trajectories captured across 2.6 km of urban roadways
- High-resolution tracking using polygon-based OBB (Oriented Bounding Box) detection
- Built-in tools for lane-change, TTC, congestion, and flow-density analysis
- Stabilized video data and real-world orthophoto-mapped trajectories
### Trajectory samples
<img src="https://github.com/user-attachments/assets/473d7545-c73c-4fd1-bc92-e818f64f872f" width="70%"/>

## Dataset Specifications
- **Site coverage**: 9 interconnected urban intersections in Daejeon, South Korea  
- **Imagery**: 4K drone footage with frame-level annotations  
- **Trajectory format**: Real-world coordinates with speed, acceleration, and heading  
- **Model**: YOLOv11m + ByteTrack with polygon-based OBB detection

## Demo Videos
<video src="https://github.com/user-attachments/assets/08aed82e-8514-4fd8-bb57-b651b7e30ff6" controls width="600">
  Your browser does not support the video tag.
</video>
<video src="https://github.com/user-attachments/assets/9c6845dd-912f-4665-b1a3-2f8d559d6723" controls width="600">
  Your browser does not support the video tag.
</video>

## Quick Start
```bash
# Clone the repository
git clone https://github.com/AIxMobility/The-DRIFT

```

## Model Customization 
```bash
# Install dependencies
pip install -r requirements.txt

# Preprocess the dataset
sh extraction/preprocessing/run.sh

# Stabilize drone video
sh extraction/stabilo/run.sh

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
├── extraction/                # Data extraction and stabilization
│   ├── preprocessing/         # Preprocessing pipeline
│   │   ├── detect_and_track.py
│   │   ├── json_to_csv.py             
│   │   ├── lane.py
│   │   ├── RoI.json
│   │   ├── run.sh
│   ├── stabilo/               # Stabilization scripts (Ack.: https://github.com/rfonod/stabilo)
│   │   ├── run.sh
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
      <td><img src="https://github.com/user-attachments/assets/8e32dcfd-0df9-4a75-abe0-0c3ee60b3123" width="70%"/></td>
    </tr>
    <tr>
      <td>Time-to-Collision (TTC)</td>
      <td><img src="https://github.com/user-attachments/assets/96c667bf-b866-4f1c-9455-2ebb37182fa6" width="70%"/></td>
    </tr>
    <tr>
      <td rowspan="2"><b>Mesoscopic</b></td>
      <td>Flow-Density Diagram </td>
      <td><img src="https://github.com/user-attachments/assets/ee73e5e9-43c1-41f2-815b-8636a587de6c" width="70%"/></td>
    </tr>
    <tr>
      <td>Time-Space Diagram </td>
      <td><img src="https://github.com/user-attachments/assets/914bcdd2-2bac-4d34-95f9-9f38852a93fe" width="70%"/></td>
    </tr>
    <tr>
      <td><b>Macroscopic</b></td>
      <td>Speed Heatmap</td>
      <td><img src="https://github.com/user-attachments/assets/b078efe9-a630-471c-aaa4-37f9f2b3e356" width="60%"/></td>
    </tr>
  </tbody>
</table>

## Citation
If you use this project in your academic research, commercial products, or any published material, please acknowledge its use by citing it.
```
TBD
```


# 📡 The DRIFT Open Dataset

## 🚀 Project Overview
**DRIFT (Drone-derived Intelligent for Traffic analysis)** is an open-source dataset designed to advance traffic behavior research through high-resolution drone imagery. It enables accurate vehicle detection, trajectory tracking, and traffic flow analysis across complex urban intersections.

## 🎯 Research Objectives
- Provide a large-scale, annotated drone dataset optimized for traffic analysis
- Support urban mobility research with pre-trained models and tools
- Enable multi-scale traffic analysis (micro, meso, macro)

## 📊 Key Contributions
- About 81,699 annotated vehicle trajectories captured over 2.6 km of urban roadways
- High-resolution vehicle tracking using OBB-based detection
- Integrated tools for lane-change, TTC, congestion, and flow-density analysis
- Stabilized video data and real-world orthophoto-mapped trajectories

## 📦 Dataset Specifications
- **Site coverage**: 9 interconnected urban intersections in Daejeon, South Korea  
- **Imagery**: 4K drone footage with frame-level annotations  
- **Trajectory format**: Real-world coordinates with speed, acceleration, and vehicle heading  
- **Model**: YOLOv11m + ByteTrack with polygon-based OBB detection

## 🗂️ Repository Structure

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
│   ├── stabilo/               # Stabilization scripts
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

## 📈 Visualizations of Traffic Analysis Tools

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
      <td><img src="https://github.com/user-attachments/assets/8e32dcfd-0df9-4a75-abe0-0c3ee60b3123" width="30%"/></td>
    </tr>
    <tr>
      <td>Time-to-Collision (TTC)</td>
      <td><img src="https://github.com/user-attachments/assets/96c667bf-b866-4f1c-9455-2ebb37182fa6" width="30%"/></td>
    </tr>
    <tr>
      <td rowspan="2"><b>Mesoscopic</b></td>
      <td>Flow-Density Diagram (Site I)</td>
      <td><img src="https://github.com/user-attachments/assets/ee73e5e9-43c1-41f2-815b-8636a587de6c" width="30%"/></td>
    </tr>
    <tr>
      <td>Time-Space Diagram (Site G)</td>
      <td><img src="https://github.com/user-attachments/assets/914bcdd2-2bac-4d34-95f9-9f38852a93fe" width="30%"/></td>
    </tr>
    <tr>
      <td><b>Macroscopic</b></td>
      <td>Speed Heatmap</td>
      <td><img src="https://github.com/user-attachments/assets/b078efe9-a630-471c-aaa4-37f9f2b3e356" width="30%"/></td>
    </tr>
  </tbody>
</table>

### [Microscopic] Lane Change (LC)
<img src="https://github.com/user-attachments/assets/8e32dcfd-0df9-4a75-abe0-0c3ee60b3123" width="30%"/>

### [Microscopic] Time-to-Collision (TTC)
<img src="https://github.com/user-attachments/assets/96c667bf-b866-4f1c-9455-2ebb37182fa6" width="30%"/>

### [Mesoscopic] Flow-Density Diagram (Site I)
<img src="https://github.com/user-attachments/assets/ee73e5e9-43c1-41f2-815b-8636a587de6c" width="30%"/>

### [Mesoscopic] Time-Space Diagram (Site G)
<img src="https://github.com/user-attachments/assets/914bcdd2-2bac-4d34-95f9-9f38852a93fe" width="30%"/>

### [Macroscopic] Speed Heatmap
<img src="https://github.com/user-attachments/assets/b078efe9-a630-471c-aaa4-37f9f2b3e356" width="30%"/>

## ⚙️ Quick Start
```bash
# Clone the repository
git clone https://github.com/AIxMobility/The-DRIFT
cd The-DRIFT

# Install dependencies
pip install -r requirements.txt

# Preprocess the dataset
sh extraction/preprocessing/run.sh

# Stabilize drone video
sh extraction/stabilo/run.sh

# Train detection model
python model/train.py
```

## Acknowledgement
This project references the open-source stabilization tool:
* https://github.com/rfonod/stabilo

## Citing This Work
If you use this project in your academic research, commercial products, or any published material, please acknowledge its use by citing it.
```
@article{noh2025drift,
  title     = {DRIFT: Drone-derived Intelligent Dataset for Urban Traffic Analysis},
  author    = {Byeongjoon Noh and et al.},
  journal   = {Under Review},
  year      = {2025},
  note      = {Available at https://github.com/AIxMobility/The-DRIFT}
}
```


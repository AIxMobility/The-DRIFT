# 📡 The DRIFT Open Dataset

## 🚀 Project Overview
**DRIFT (Drone-derived Intelligent for Traffic analysis)** is an open-source dataset designed to advance traffic behavior research through high-resolution drone imagery. It enables accurate vehicle detection, trajectory tracking, and traffic flow analysis across complex urban intersections.

## 🎯 Research Objectives
- Provide a large-scale, annotated drone dataset optimized for traffic analysis
- Support urban mobility research with pre-trained models and tools
- Enable multi-scale traffic analysis (micro, meso, macro)

## 📊 Key Contributions
- 81,699 annotated vehicle trajectories captured over 2.6 km of urban roadways
- High-resolution vehicle tracking using OBB-based detection
- Integrated tools for lane-change, TTC, congestion, and flow-density analysis
- Stabilized video data and real-world orthophoto-mapped trajectories

## 📦 Dataset Specifications
- **Site coverage**: 9 interconnected urban intersections in Daejeon, South Korea  
- **Imagery**: 4K drone footage with frame-level annotations  
- **Trajectory format**: Real-world coordinates with speed, acceleration, and vehicle heading  
- **Model**: YOLOv8 + ByteTrack with polygon-based OBB detection

## 🗂️ Repository Structure (Sample)

```DroneTrack/
│
├── data/                      # Raw and processed drone data
│   ├── csv/                   # Drone footage metadata
│   ├── sample_video/          # Sample drone videos
│   ├── site_images/           # Site-specific images from drone footage
│
├── extraction/                # Data extraction and stabilization
│   ├── preprocessing/         # Scripts for data preprocessing
│   │   ├── detect_and_track.py
│   │   ├── json_to_csv.py             
│   │   ├── lane.py
│   │   ├── RoI.json
│   │   ├── run.sh
│   ├── stabilo/               # Stabilization-related scripts
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

## 🔍 Visualization

### Flow density relationship & ROI information
![Image](https://github.com/user-attachments/assets/ee73e5e9-43c1-41f2-815b-8636a587de6c)

### LC
![Image](https://github.com/user-attachments/assets/8e32dcfd-0df9-4a75-abe0-0c3ee60b3123)

### Speed-heatmap
![Image](https://github.com/user-attachments/assets/b078efe9-a630-471c-aaa4-37f9f2b3e356)

### Time-space diagram of Site G
![Image](https://github.com/user-attachments/assets/914bcdd2-2bac-4d34-95f9-9f38852a93fe)

### TTC
![Image](https://github.com/user-attachments/assets/96c667bf-b866-4f1c-9455-2ebb37182fa6)


## 📈 Utilized Tools fot Traffic Analysis
* for KAIST


## 🚀 Quick Start 
```python
# Clone the repository
git clone https://github.com/AIxMobility/The-DRIFT

# Install dependencies
pip install -r requirements.txt

# Preprocess dataset
sh extraction/preprocessing/run.sh

# Stabilization video
sh extraction/stabilo/run.sh

# Train detection model
python model/train.py
```
## Acknowledgement
* https://github.com/rfonod/stabilo

## Citing This Work
If you use this project in your academic research, commercial products, or any published material, please acknowledge its use by citing it.
```
?
```


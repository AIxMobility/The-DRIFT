# The DRIFT Open Dataset

## 🚀 Project Overview
The DRIFT is comprehensive open-source research project focusing on advanced vehicle detection, tracking, and traffic pattern analysis using high-resolution drone imagery across diverse urban and rural environments.


### 📊 Key Research Contributions (Sample)
* Large-scale drone-captured vehicle detection dataset
* Advanced deep learning models for real-time vehicle tracking
* Comprehensive traffic flow and congestion analysis algorithms

### 🔬 Research Objectives (Sample)
* Provide a standardized, annotated drone dataset for traffic analysis
* Provide open-source tools for urban mobility research

## 📦 Dataset Specifications
* Site information
* Recorded video information
* Provided dataset information
* Used model information

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


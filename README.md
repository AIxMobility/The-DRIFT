# The-DRIFT

## 🚀 Project Overview
The DRIFT is comprehensive open-source research project focusing on advanced vehicle detection, tracking, and traffic pattern analysis using high-resolution drone imagery across diverse urban and rural environments.


## 📊 Key Research Contributions (Sample)

* Large-scale drone-captured vehicle detection dataset
* Advanced deep learning models for real-time vehicle tracking
* Comprehensive traffic flow and congestion analysis algorithms

## 🔬 Research Objectives (Sample)
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
│   │   ├── detect-and-track.py
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
|
├── utils/                     # Utility scripts for data handling
│   ├── convert.py
│
├── viz/                       # Visualization scripts and tools
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── performance_analysis.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE

```

## 📈 Utilized Tools fot Traffic Analysis
* for KAIST


## 🚀 Quick Start 
```python
# Clone the repository
git clone https://github.com/AIxMobility/The-DRIFT

# Install dependencies
pip install -r requirements.txt

# Preprocess dataset
sh ./extraction/preprocessing/run.sh

# Stabilization video
sh ./extraction/stabilo/run.sh

# Train detection model
python model/train.py
```




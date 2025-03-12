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
├── data/
│   ├── csv/                   # Original drone footage
│   ├── sample_video/           # Detailed vehicle annotations
│   ├── site_images/
│
├── extraction/
│   ├── preprocessing/          # Data preprocessing pipeline
│   │   ├── detect-and-track.py
│   │   ├── json_to_csv.py             # Lane processing script
│   │   ├── lane.py
│   │   ├── RoI.json
│   │   ├── run.sh
│   ├── stabilo/                
│   │   ├── run.sh
|
├── model/
│   ├── test/                   
│   ├── train/           
│   ├── valid/
│   ├── data.yaml                   
│   ├── drone_data.yaml           
│   ├── train.py
|
├── utils/
│   ├── convert.py
│
├── viz/
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




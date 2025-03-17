
# Extraction

## 🗂️ Repository Structure (Sample)

```DroneTrack/

├── extraction/                # Data extraction and stabilization
│   ├── preprocessing/         # Scripts for data preprocessing
│   │   ├── detect_and_track.py
│   │   ├── json_to_csv.py             
│   │   ├── lane.py
│   │   ├── RoI.json
│   │   ├── run.sh
│   ├── stabilo/               # Stabilization-related scripts
│   │   ├── run.sh
│   ├── geoalign/ 
│   │   ├── geoalign_transformation.ipynb
│   │   ├── geoalign_roi.json

```

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

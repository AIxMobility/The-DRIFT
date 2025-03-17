
# Extraction

## 🗂️ Repository Structure

```DroneTrack/
├── extraction/                # Data extraction and stabilization
│   ├── geoalign/
│   │   ├── geoalign_roi.json
│   │   ├── geoalign_transformation.ipynb
│   │
│   ├── preprocessing/         # Scripts for data preprocessing
│   │   ├── detect_and_track.py
│   │   ├── json_to_csv.py             
│   │   ├── lane.py
│   │   ├── roi.json
│   │   ├── run.sh
│   │
│   ├── stabilo/               # Stabilization-related scripts
│   │   ├── run.sh
```

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

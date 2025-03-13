import requests
import zipfile
import os
import yaml
import jsonschema
from ultralytics import YOLO
import ultralytics
import torch

torch.cuda.is_available()

extraction_directory = './model'

for item in os.listdir(extraction_directory):
    print(item)

data = { 'train' : './model/train/images',
        'val' : './model/valid/images/',
        'test' : './model/test/images/',
        'names' : ['bus', 'car', 'truck'],
        'nc' : 3 }

with open('./model/drone_data.yaml', 'w') as f:
    yaml.dump(data, f)
    
with open('./model/drone_data.yaml', 'r') as f:
    Drone_yaml = yaml.safe_load(f)
    print(Drone_yaml)

ultralytics.checks()

model = YOLO('./model/yolo11m-obb.pt')

print(type(model.names), len(model.names))
print(model.names)

model.train(data = './model/drone_data.yaml', epochs = 500, patience = 50, batch = 4, imgsz = 1920)
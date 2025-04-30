#!/bin/bash

# Setting
export VIDEO_PATHS="./data/sample_video/DJI_0025_cut1.MP4"
export SCRIPT_PATH="./preprocessing/scripts/stabilize_video.py"
export OPTIONS="--save --no-mask"
export REF_FRAME_PATH="./data/site_images/SiteB.jpg"

CUDA_VISIBLE_DEVICES=0 python3 "$SCRIPT_PATH" "$VIDEO_PATHS" --ref-frame "$REF_FRAME_PATH" $OPTIONS
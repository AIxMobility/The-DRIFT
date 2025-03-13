#!/bin/bash

# Setting
export VIDEO_PATHS="./data/sample video/DJI_0008_cut.MP4"
export SCRIPT_PATH="./extraction/stabilo/scripts/stabilize_video.py"
export OPTIONS="--save --no-mask"
export REF_FRAME_PATH="./data/site images/SiteB.jpg"

CUDA_VISIBLE_DEVICES=0 python3 "$SCRIPT_PATH" "$VIDEO_PATHS" --ref-frame "$REF_FRAME_PATH" $OPTIONS

import os
import subprocess

# Setting example
VIDEO_PATHS = "./data/sample_video/DJI_0025_cut1.Mp4"
SCRIPT_PATH = "./preprocessing/stabilo/scripts/stabilize_video.py"
OPTIONS = "--save --no-mask"
REF_FRAME_PATH = "./data/site_images/SiteB.jpg"

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

command = f'python3 "{SCRIPT_PATH}" "{VIDEO_PATHS}" --ref-frame "{REF_FRAME_PATH}" {OPTIONS}'

subprocess.run(command, shell=True, check=True)

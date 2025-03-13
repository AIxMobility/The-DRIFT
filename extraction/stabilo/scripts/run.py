import os
import subprocess


video_paths = [
    """
    your video path
    ./data/Sample video/DJI_0008_cut.MP4
    """
]

# stabilizer.py 경로 및 추가 옵션
script_path = "stabilize_video.py"
options = ["--save-viz", "--no-mask"]

# 참조 프레임 경로 설정
ref_frame_path = "./data/site images/SiteB.jpg"

# 각 비디오 경로에 대해 stabilizer 실행
for video_path in video_paths:
    print(f"Processing: {video_path}")
    try:
        # subprocess 호출에 ref-frame 추가
        subprocess.run(["python", script_path, video_path, "--ref-frame", ref_frame_path, *options], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing {video_path}: {e}")

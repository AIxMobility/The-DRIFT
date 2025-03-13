import cv2
import os

def extract_frames(video_path, output_path, frame_interval=1):
    """
    Extract frames from a video and save them to a specified directory.
    :param video_path: Path to the input video file
    :param output_path: Directory where frames will be saved
    :param frame_interval: Interval at which frames are saved (default: 1)
    """
    os.makedirs(output_path, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_count = 0  # Total frame count
    saved_count = 0  # Saved frame count
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break  
        
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_path, f"frame_{saved_count:06d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"Total frames extracted: {saved_count}")

if __name__ == "__main__":
    video_path = "./data/sample_video/DJI_0008_cut.MP4"  # Path to the input video
    output_path = "./data/frames_output"    # Directory to save frames
    frame_interval = 5                # Frame interval for saving (default: 1)
    
    extract_frames(video_path, output_path, frame_interval)

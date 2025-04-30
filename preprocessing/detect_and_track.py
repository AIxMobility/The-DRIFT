import cv2
from ultralytics import YOLO
import torch
import json
import os
import argparse

def main(model_path, input_videos, output_json_dir):
    # Load YOLOv11 OBB model
    model = YOLO(model_path, task="obb")

    # Confidence threshold to set
    confidence_threshold = 0.8

    # Create the save directory if it does not exist
    os.makedirs(output_json_dir, exist_ok=True)

    for video_path in input_videos:
        cap = cv2.VideoCapture(video_path)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count = 0

        vehicle_data = []

        # Extract video file name
        video_name = os.path.splitext(os.path.basename(video_path))[0]

        while cap.isOpened() and frame_count < total_frames:
            ret, frame = cap.read()
            if not ret:
                break

            # Input frame to the model and perform tracking
            results = model.track(source=frame, conf=confidence_threshold, tracker='bytetrack.yaml', show=False, persist=True, line_width=1)

            for result in results:
                vehicle_frame_info = {
                    "frame": frame_count,
                    "obb": []  # Store OBB information
                }

                if result.obb is not None:
                    for obb in result.obb:
                        xywhr = obb.data[:, :5]
                        conf = obb.conf
                        cls = obb.cls
                        ids = obb.id
                        xyxyxyxy = obb.xyxyxyxy

                        for i in range(len(xywhr)):
                            cx, cy, w, h, theta = map(float, xywhr[i])
                            confidence = float(conf[i])
                            class_id = int(cls[i])
                            track_id = int(ids[i])
                            points = xyxyxyxy[i].flatten().tolist()
                            x1, y1, x2, y2, x3, y3, x4, y4 = map(float, points)

                            vehicle_frame_info["obb"].append({
                                "center": (cx, cy),
                                "polygon": (x1, y1, x2, y2, x3, y3, x4, y4),
                                "dimensions": (w, h),
                                "angle": theta,
                                "confidence": confidence,
                                "class_id": class_id,
                                "track_id": track_id
                            })

                vehicle_data.append(vehicle_frame_info)

            frame_count += 1

        # Save JSON file
        vehicle_output_path = os.path.join(output_json_dir, f"{video_name}.json")
        with open(vehicle_output_path, 'w') as f:
            json.dump(vehicle_data, f, indent=4)

        cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 OBB Video Inference")

    parser.add_argument(
        "--model", 
        type=str, 
        required=True, 
        help="Path to the YOLOv11 OBB model"
    )
    parser.add_argument(
        "--input", 
        type=str, 
        nargs='+', 
        required=True, 
        help="Path(s) to input video file(s)"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        required=True, 
        help="Directory to save output JSON files"
    )

    args = parser.parse_args()

    main(args.model, args.input, args.output)

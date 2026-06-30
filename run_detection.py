"""
DroneScan - Detection Module (skeleton)

Runs the object detection pipeline on a video source (file or live stream)
and outputs bounding boxes + class labels per frame.

See docs/chapter4 and docs/chapter6 for the full walkthrough.
"""
import argparse


def run_detection(source: str, model_path: str = "models/detector.onnx", conf_threshold: float = 0.5):
    """Run real-time object detection on the given video source.

    TODO:
        - Load the detection model (see docs/chapter4)
        - Open the video source with OpenCV / GStreamer
        - For each frame: preprocess -> infer -> postprocess (NMS)
        - Yield or display detections
    """
    raise NotImplementedError("Implement detection pipeline — see docs/chapter4")


def main():
    parser = argparse.ArgumentParser(description="Run DroneScan object detection on a video source")
    parser.add_argument("--source", required=True, help="Path to video file or stream URL")
    parser.add_argument("--model", default="models/detector.onnx", help="Path to detection model")
    parser.add_argument("--conf", type=float, default=0.5, help="Confidence threshold")
    args = parser.parse_args()
    run_detection(args.source, args.model, args.conf)


if __name__ == "__main__":
    main()

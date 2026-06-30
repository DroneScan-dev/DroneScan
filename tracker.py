"""
DroneScan - Multi-Object Tracking Module (skeleton)

Assigns persistent track IDs to detections across frames and maintains
movement trails. See docs/chapter8.
"""


class Tracker:
    def __init__(self, max_age: int = 30, iou_threshold: float = 0.3):
        self.max_age = max_age
        self.iou_threshold = iou_threshold
        self.tracks = {}

    def update(self, detections):
        """Update tracks with the latest frame's detections.

        TODO: implement IOU/Kalman-based association (see docs/chapter8)
        """
        raise NotImplementedError("Implement tracker update — see docs/chapter8")

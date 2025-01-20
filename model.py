from roboflow import Roboflow
rf = Roboflow(api_key="vml8GLVteqwrzuCHy2zp")
project = rf.workspace("frc-5881-yho3d").project("2025-reefscape")
version = project.version(11)
dataset = version.download("yolov8")
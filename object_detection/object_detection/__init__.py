"""
Object detection package:

    # Model initialization
    model = DetectionModel(model_weights='models/yolov4.weights',
                           model_config='models/yolov4.cfg',
                           confidence_threshold=0.5, nms_threshold=0.5)

    # Detection function
    detections = model(frame)
        or
    detections = model.detect(frame=img)

    # Detected objects
    objects = detections.get_objects(ignore_other=True)

    # Annotated frame
    frame = detections.get_frame(ignore_other=True)

YOLOv4:
    https://github.com/AlexeyAB/darknet/wiki/YOLOv4-model-zoo
    Weights : https://drive.google.com/file/d/1L-SO373Udc9tPz5yLkgti5IAXFboVhUt/view
    Config  : https://drive.google.com/file/d/1hSrVqiEbuVewEIVU4cqG-SqJFUNTYmIC/view

"""
from .detection_model import DetectionModel

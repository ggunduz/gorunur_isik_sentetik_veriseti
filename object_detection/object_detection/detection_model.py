import cv2

from .interpreter import Interpreter
from .detected_object import Detection


class DetectionModel:

    def __init__(self, model_weights, model_config=None,
                 confidence_threshold=0.5, nms_threshold=0.5,
                 input_shape=(512, 512), scale=1/255, swap_rb=True):

        """
        The object detection model uses the OpenCV or TFLite framework.
        If the config file is none, TFLite interpreter runs.
        :param model_weights: Binary file contains trained weights.
        :param model_config: Text file contains network configuration.
        :param confidence_threshold: A threshold used to filter boxes by confidences.
        :param nms_threshold: A threshold used in non maximum suppression.
        :param input_shape: Input shape.
        :param scale: Multiplier for frame values.
        :param swap_rb: Flag which indicates that swap first and last channels.
        """

        if model_config is not None:
            net = cv2.dnn.readNet(model_weights, model_config)
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

            self.model = cv2.dnn_DetectionModel(net)
            self.model.setInputParams(size=input_shape, scale=scale, swapRB=swap_rb)

        else:  # TFLite model
            self.model = Interpreter(model_path=model_weights)

        self.confidence_threshold = confidence_threshold
        self.nms_threshold = nms_threshold

    def __call__(self, frame):
        """
        Call detect function.
        :param frame: The input image.
        :return: Return value of detect function.
        """
        return self.detect(frame)

    def detect(self, frame):
        """
        Detects objects in the frame and returns in an object struct.
        :param frame: The input image.
        :return: Detection object for frame.
        """
        classes, scores, boxes = self.model.detect(frame, self.confidence_threshold, self.nms_threshold)
        return Detection(frame=frame, classes=classes, scores=scores, bounding_boxes=boxes)

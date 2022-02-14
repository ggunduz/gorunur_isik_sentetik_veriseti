
import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image

from .nms import non_max_suppression


class Interpreter:

    def __init__(self, model_path):
        """
        TFLite model interpreter.
        :param model_path: Model path (.tflite).
        """
        self.interpreter = tflite.Interpreter(model_path=model_path)

        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    @property
    def shape(self):
        """
        Return shape of the pre-trained model input
        :return: Input shape (width, height)
        """
        height = self.input_details[0]['shape'][1]
        width = self.input_details[0]['shape'][2]
        return width, height

    def invoke(self, input_data):
        """
        Feed-forward input data and return model output.
        :param input_data: Input data
        :return: Model output
        """
        # Inference
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        return self.interpreter.get_tensor(self.output_details[0]['index'])

    def detect(self, frame, confidence_threshold=0.5, nms_threshold=0.5):
        """
        Detect objects in the frame and return classes, confidence scores and bounding boxes.
        :param frame: Input image
        :param confidence_threshold: Confidence threshold
        :param nms_threshold: Non-max suppression threshold, (Intersection Over Union)
        :return: Classes, scores and boxes of detected objects
        """
        # Prepare input
        frame = Image.fromarray(frame)
        input_data = frame.resize(self.shape)
        input_data = np.expand_dims(input_data, axis=0).astype(dtype=self.input_details[0]['dtype'])
        input_data = input_data[:, :, :, :3]

        if input_data.dtype.kind == 'f':
            input_data = input_data / 255

        # Inference
        output_data = self.invoke(input_data=input_data)

        # Confidence threshold
        predictions = np.squeeze(output_data)
        predictions = predictions[predictions[..., 4] > confidence_threshold]

        # Output format
        boxes = predictions[..., 0:4]

        # Center of object to top-left
        boxes[..., 0] = boxes[..., 0] - boxes[..., 2] / 2
        boxes[..., 1] = boxes[..., 1] - boxes[..., 3] / 2

        # Rescale bounding boxes
        boxes[..., 0] *= frame.size[0]  # x
        boxes[..., 1] *= frame.size[1]  # y
        boxes[..., 2] *= frame.size[0]  # w
        boxes[..., 3] *= frame.size[1]  # h

        scores = predictions[..., 4]
        classes = predictions[..., 5:].argmax(axis=1).astype(dtype=np.int)

        picks = non_max_suppression(boxes=boxes, scores=scores, iou_threshold=nms_threshold)

        return classes[picks], scores[picks], boxes[picks].astype(dtype=np.int)

import glob
import os
import time

import cv2

from object_detection import DetectionModel


if __name__ == '__main__':

    print(cv2.__version__)


    #model = DetectionModel(model_weights='models/yolov4-tiny.weights', model_config='models/yolov4-tiny.cfg',
    #                       confidence_threshold=0.5, nms_threshold=0.5, input_shape=(416, 416))

    model = DetectionModel(model_weights='models/lite-model_yolo-v5-tflite_tflite_model_1.tflite',
                           confidence_threshold=0.5, nms_threshold=0.5)
    
    
    path = "camera/{0:03d}.jpg".format(recorded_alarm_number+1)
    
    frame = cv2.imread(path)
    
    #cam = cv2.VideoCapture(0)

    #while True:
    #    ret, frame = cam.read()
	
    start = time.time()
    detections = model.detect(frame=frame)
    end = time.time()
    
    objects = detections.get_objects(ignore_other=True)
    
    print(objects)
	
    #    frame = detections.get_frame(ignore_other=False)
	
    #    cv2.imshow('Camera', frame)

    print(f"\rFPS: {1/(end-start):.2f}", end='')

    #    if cv2.waitKey(1) == ord('q'):
    #        break
   
    #cam.release()
    #cv2.destroyAllWindows()
    #print('\nclosed')

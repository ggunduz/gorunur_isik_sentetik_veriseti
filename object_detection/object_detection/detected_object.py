import cv2

from .class_map import get_class_name, get_class_color


class Detection:

    def __init__(self, frame, classes, scores, bounding_boxes):
        """
        Detection object for a frame.
        :param frame: The image.
        :param classes: Detected classes.
        :param scores: Confidence scores of classes.
        :param bounding_boxes: Bounding boxes of classes.
        """
        self.frame = frame
        self.classes = classes
        self.scores = scores
        self.bounding_boxes = bounding_boxes

    def get_objects(self, ignore_other=True):
        """
        Return object map with count and maximum confidence score
        :type ignore_other: Ignore 'other' class in the object map
        :return: Object map: {
                    <class_name> : { count: <number of objects>,
                                     max_score: <maximum confidence score of detected objects> }
                    ...
                    }
        """

        object_map = dict()

        for class_id, score in zip(self.classes, self.scores):
            class_name = get_class_name(class_id)

            if ignore_other and class_name == 'other':
                continue

            if class_name not in object_map:
                object_map[class_name] = {'count': 0, 'max_score': 0.0}

            object_map[class_name]['count'] += 1
            object_map[class_name]['max_score'] = max(object_map[class_name]['max_score'], float(score))

        return object_map

    def get_ids(self, ignore_other=True):
        """
        Return object map with count and maximum confidence score
        :type ignore_other: Ignore 'other' class in the object map
        :return: Object map: {
                    <class_name> : { count: <number of objects>,
                                     max_score: <maximum confidence score of detected objects> }
                    ...
                    }
        """

        object_map = dict()

        for class_id, score in zip(self.classes, self.scores):


            if ignore_other and class_id == 0:
                continue

            if class_id not in object_map:
                object_map[class_id] = {'count': 0, 'max_score': 0.0}

            object_map[class_id]['count'] += 1
            object_map[class_id]['max_score'] = max(object_map[class_id]['max_score'], float(score))

        return object_map

    def get_frame(self, annotations=True, ignore_other=True):
        """
        Get raw frame or with annotations (classes and bounding boxes).
        :param annotations: Boolean, if true draw annotations on frame.
        :param ignore_other: Ignore 'other' class in the annotated frame
        :return: Raw or annotated frame.
        """
        annotated_frame = self.frame
        if annotations:
            for class_id, score, box in zip(self.classes, self.scores, self.bounding_boxes):
                class_name = get_class_name(class_id)

                if ignore_other and class_name == 'other':
                    continue

                color = get_class_color(class_name)
                label = f'{class_name} : {score}'

                pt1, pt2 = (box[0], box[1]), (box[0]+box[2], box[1]+box[2]) 
                cv2.rectangle(annotated_frame, pt1, pt2, color, 2)
                cv2.putText(annotated_frame, label, (box[0] + 4, box[1] + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        return annotated_frame

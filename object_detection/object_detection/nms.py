import numpy as np


def overlapping_area(detection1, detection2):
    """
    Calculate ratio of overlapping to total area.
    :param detection1: Bounding box of first detection
    :param detection2: Bounding box of second detection
    :return: Overlap area divided by total area
    """
    # Detection 1
    x1_tl = detection1[0]
    x1_br = detection1[0] + detection1[2]
    y1_tl = detection1[1]
    y1_br = detection1[1] + detection1[3]
    area1 = detection1[2] * detection1[3]

    # Detection 2
    x2_tl = detection2[0]
    x2_br = detection2[0] + detection2[2]
    y2_tl = detection2[1]
    y2_br = detection2[1] + detection2[3]
    area2 = detection2[2] * detection2[3]

    # Calculate the overlapping Area
    x_overlap = max(0, min(x1_br, x2_br) - max(x1_tl, x2_tl))
    y_overlap = max(0, min(y1_br, y2_br) - max(y1_tl, y2_tl))

    overlap_area = x_overlap * y_overlap
    total_area = area1 + area2 - overlap_area

    return overlap_area / total_area


def non_max_suppression(boxes, scores=None, iou_threshold=0.5):
    """
    Apply non-max suppression for detected bounding boxes with respect to confidence score.
    :param boxes: Bounding boxes
    :param scores: Confidence scores
    :param iou_threshold: Intersection Over Union threshold
    :return: Selected indices
    """
    selected_indices = list()

    if len(boxes) == 0:
        return selected_indices

    detected_indices = np.arange(len(boxes))
    if scores is not None:
        detected_indices = [x for _, x in sorted(zip(scores, detected_indices), key=lambda pair: pair[0])]

    selected_indices.append(detected_indices[0])

    for detected_index in detected_indices[1:]:
        if not any([overlapping_area(boxes[detected_index], boxes[selected_index]) > iou_threshold
                    for selected_index in selected_indices]):
            selected_indices.append(detected_index)

    return selected_indices

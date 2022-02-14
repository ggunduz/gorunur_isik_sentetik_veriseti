
CLASS_MAP = {
    0: 'person',

    1: 'vehicle',
    2: 'vehicle',
    3: 'vehicle',
    4: 'vehicle',
    5: 'vehicle',
    6: 'vehicle',
    7: 'vehicle',
    8: 'vehicle',

    14: 'animal',
    15: 'animal',
    16: 'animal',
    17: 'animal',
    18: 'animal',
    19: 'animal',
    20: 'animal',
    21: 'animal',
    22: 'animal',
    23: 'animal',
}

COLOR_MAP = {'person':  (0, 255, 255),
             'vehicle': (255, 255, 0),
             'animal':  (0, 255, 0),
             'other':   (255, 0, 0)}


def get_class_name(class_id):
    """
    Return class name for class ID, if it is not defined return 'other'.
    :param class_id: Predicted class ID.
    :return: Class name.
    """
    try:
        return CLASS_MAP[int(class_id)]
    except KeyError:
        return 'other'


def get_class_color(class_name):
    """
    Return class color for class ID, if it is not defined return 'other' color.
    :param class_name: Class name.
    :return: Class color.
    """
    try:
        return COLOR_MAP[class_name]
    except KeyError:
        return COLOR_MAP['other']

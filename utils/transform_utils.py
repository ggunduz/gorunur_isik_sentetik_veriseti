import cv2
import random
from scipy import ndimage
import numpy as np

def transform_object_and_mask(image,
                            mask,
                            rotation = None,
                            ):


    availible_transforms = [
                            'horizontal_flip',
                            'none',
                            'scale',
                        ]

    choosen_transform = random.choice(availible_transforms)


    if choosen_transform == 'horizontal_flip':
        image = cv2.flip(image, 1)
        mask = cv2.flip(mask, 1)

    elif choosen_transform == 'scale':

        scales = [0.5, 0.75, 1.25, 1.5]
        choose_scale = random.choice(scales)

        h, w = image.shape[:2]
        new_h = int(h*choose_scale)
        new_w = int(w*choose_scale)

        image = cv2.resize(image, (new_w, new_h))
        mask = cv2.resize(mask, (new_w, new_h))
  
    rotation = random.choice(list(range(-15,15)))

    image = ndimage.rotate(image, rotation)
    mask = ndimage.rotate(mask, rotation)
    
    return image , mask


def get_transformed_object_patch(image_new,
                                mask_new,
                                background_image_shape):


    y, x = np.where(mask_new == 1)
    object_height = y.max()-y.min()
    object_width = x.max()-x.min()

    patch = image_new[y,x]

    y = y-y.min()
    x = x-x.min()

    maximum_possible_y = background_image_shape[0]-2-object_height
    maximum_possible_x = background_image_shape[1]-2-object_width

    return patch, y, x, maximum_possible_y, maximum_possible_x


def place_transformed_object_patch(random_background_image,
                                    patch,
                                    y,
                                    x,
                                    maximum_possible_y,
                                    maximum_possible_x,):



    possible_x = random.choice(range(maximum_possible_x))
    possible_y = random.choice(range(maximum_possible_y))
    
    random_background_image[y + possible_y,
                            x + possible_x] = patch
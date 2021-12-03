import random
import cv2
import os


def load_random_background_image(DATA_DIR = './data/',
                                ):

    background_images = os.listdir(DATA_DIR + './background/')
    random_background_image = random.choice(background_images)
    random_background_image = cv2.imread(DATA_DIR + './background/' + random_background_image)

    #background_height, background_width = random_background_image.shape[:2]

    return random_background_image, random_background_image.shape[:2]
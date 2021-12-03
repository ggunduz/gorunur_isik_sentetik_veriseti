import albumentations as A
from albumentations import  Compose, OneOf

def apply_augmentation(image):

    transform = A.Compose([


    OneOf([
           A.RandomSnow(p=0.5),
           A.RandomShadow(p=0.5),
           A.RandomSunFlare(p=0.5),
       ], p=0.5),

    #A.RandomCrop(width=256, height=256),
    A.Blur(p=0.2),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])



    transformed = transform(image=image)
    transformed_image = transformed["image"]


    return transformed_image

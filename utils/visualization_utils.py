import cv2
import matplotlib.pyplot as plt

def visualize_original_image_and_mask(original_image,
                                    mask,
                                    figsize = (10,10),
                                    transform_type = ""):

    fig = plt.figure(figsize=(figsize))

    ax = fig.add_subplot(1, 2, 1)
    ax.set_title("Original Image %s" % transform_type)
    ax.imshow(original_image[:,:,::-1])

    ax.set_yticklabels([])
    ax.set_xticklabels([])

    ax = fig.add_subplot(1, 2, 2)
    ax.set_title("Object Mask %s" % transform_type)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.imshow(mask)

    fig.tight_layout()

    plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(filepath: str):
    return cv2.imread(filepath)


def display_image(image: np.ndarray):
    plt.imshow(image, interpolation='none')
    plt.show()


def convert_color_space(image: np.ndarray, _from: str, _to: str):
    from_to = {
        'BGR': {
          'RGB': cv2.COLOR_BGR2RGB
        }
    }

    conversion_code = from_to[_from][_to]
    return cv2.cvtColor(image, conversion_code)


def read_RGB_image(filepath: str):
    image = cv2.imread(filepath)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def transpose_image():
    pass

# def extract_red_green_blue(image: np.ndarray):
#     """
#     Usage: red_channel, green_channel, blue_channel = extract_red_green_blue(image)
#     """
#     return cv2.split(image)

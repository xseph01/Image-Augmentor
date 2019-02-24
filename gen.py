import Augmentor
import os
from tqdm import tqdm

IMG_PATH = 'C:/Users/xseph/Documents/meat1'
CLASSIFICATIONS = ["beefHealthy", "beefFair", "beefSpoiled", "chickenHealthy", "chickenFair", "chickenSpoiled",
                   "porkHealthy", "porkFair", "porkSpoiled"] # Change this with your folder name

for classifications in CLASSIFICATIONS:
    try:
        p = Augmentor.Pipeline(IMG_PATH + "/" + classifications)
        p.skew(probability=0.4)
        p.random_distortion(probability=0.2, grid_width=4, grid_height=4, magnitude=8)
        p.rotate(probability=0.5, max_left_rotation=25, max_right_rotation=25)
        p.shear(probability=0.25, max_shear_left=25, max_shear_right=25)
        p.flip_random(probability=0.5)
        p.crop_random(probability=1, percentage_area=0.5)
        p.zoom_random(probability=.5, percentage_area=0.50)
        p.random_brightness(probability=.5, min_factor=1, max_factor=2)
        p.random_contrast(probability=.5, min_factor=1, max_factor=2)
        p.resize(probability=1.0, width=128, height=128)
        p.sample(10000)
    except Exception as e:
        pass

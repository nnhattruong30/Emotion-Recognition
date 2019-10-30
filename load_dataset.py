import pandas as pd
import cv2
import np as np

dataset_path = 'dataset/fer2013.csv'
image_size = (48,48)

def load_dataset():
    
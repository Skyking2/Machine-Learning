#Import necessary libraries
import os
import cv2
import numpy as np
from tqdm import tqdm
import torch
import torch.nn as nn
from random import shuffle

TRAIN_DIR = 'FILL_ME'
TEST_DIR = 'FILL_ME'
IMG_SIZE = 50
LR = 1e-3 #Learning rate


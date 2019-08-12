from collections import deque
import cv2
import imutils
import numpy as np
import time

class Tracker:
    def __init__(self):
        # What mode?
        self.mode = 'learn'
        # Propertieis about the learnt object
        self.typical_rgb = [0, 0, 0]
        self.max_rgb = [0, 0, 0]
        self.min_rgb = [0, 0, 0]
        # Properties about the tracked object
        self.location = [0, 0]
        self.size = [0, 0]
        self.angle = 0
        self.last_seen = 0


    def new_image(image_source):
        if self.mode = 'learn':
            self._learn_block(image_source)
        elif self.mode = 'tracker':
            self._get_block(image_source)

    def _learn_block(image_source):
        pass

    def _get_block(image_source):
        pass

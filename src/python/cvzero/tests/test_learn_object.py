import os
import unittest
import Library.cvzero as cvzero


class TestTrackObject(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        #
        self.test_img1 = os.path.join(self.test_dir, 'images', 'object_1.raw')
        self.tracker = cvzero.Tracker()
        self.tracker.mode = 'learn'

    def test_object_colour(self):
        self.tracker.new_image(self.test_img1)
        self.assertEqual([105, 50, 50], self.tracker.min_rgb,
                         'Error in minimum RGB found in image')
        self.assertEqual([130, 255, 255], self.tracker.max_rgb,
                         'Error in maximum RGB found in image')

import os
import unittest
import Library.cvzero as cvzero


class TestTrackObject(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        #
        self.test_img1 = os.path.join(self.test_dir, 'images', 'object_1.raw')
        self.tracker = cvzero.Tracker()
        self.tracker.mode = 'tracker'

    def test_find_object(self):
        self.tracker.min_rgb = [105, 50, 50]
        self.tracker.max_rgb = [130, 255, 255]
        self.tracker.new_image(self.test_img1)
        self.assertEqual([30, 28], self.tracker.location,
                         'Error in location of detected object')
        self.assertEqual([44, 77], self.tracker.size,
                         'Error in size of detected object')

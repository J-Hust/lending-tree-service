import unittest
from src import review_controller


class TestReviewController(unittest.TestCase):

    def test_url_validation(self):
        bad_url = 'http://www.mountainproject.com'
        is_valid = review_controller.is_valid_url(bad_url)

        self.assertEqual(is_valid, False)

        good_url = 'https://www.lendingtree.com/reviews/personal/cashnetusa/81638970'
        is_valid = review_controller.is_valid_url(good_url)

        self.assertEqual(is_valid, True)

import unittest
from src import review_controller


class TestReviewController(unittest.TestCase):

    def test_url_validation_bad_url(self):
        bad_url = 'http://www.mountainproject.com'
        is_valid = review_controller.is_valid_url(bad_url)

        self.assertEqual(is_valid, False)

    def test_url_validation_good_url(self):
        good_url = 'https://www.lendingtree.com/reviews/personal/cashnetusa/81638970'
        is_valid = review_controller.is_valid_url(good_url)

        self.assertEqual(is_valid, True)

    def test_extract_lender_id(self):
        url = 'https://www.lendingtree.com/reviews/personal/cashnetusa/81638970'
        lender_id = review_controller.extract_lender_id_from_url(url)

        self.assertEqual(lender_id, 81638970)
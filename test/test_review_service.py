import unittest
from src import review_service


# should not rely on changing data from the internet :(
class TestReviewService(unittest.TestCase):

    def test_retrieve_reviews(self):
        r = review_service.retrieve_reviews(42825)

        self.assertEqual(len(r), 1662)
        self.assertEqual(isinstance(r, list), True)

    def test_fetch_review_list(self):
        r = review_service.fetch_review_list(42825, 1)

        self.assertEqual(isinstance(r, list), True)
        self.assertEqual(len(r), 300)

    def test_retrieve_brand_id(self):
        brand_id = review_service.retrieve_brand_id(81638970)
        self.assertEqual(brand_id, 42825)
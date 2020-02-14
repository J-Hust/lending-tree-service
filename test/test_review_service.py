import unittest
from src import review_service


# should not rely on changing data from the internet :(
class TestReviewService(unittest.TestCase):

    def test_fetch_review_count(self):
        review_count = review_service.fetch_review_count(42825)

        self.assertEqual(review_count, 1662)

    def test_iterate_reviews(self):
        r = review_service.iterate_reviews(42825)

        self.assertEqual(isinstance(r, list), True)

    def test_fetch_review_details(self):
        r = review_service.fetch_review_details(42825, 1)

        self.assertEqual(isinstance(r, list), True)
        self.assertEqual(len(r), 300)

    def test_retrieve_brand_id(self):
        brand_id = review_service.retrieve_brand_id(81638970)
        self.assertEqual(brand_id, 42825)
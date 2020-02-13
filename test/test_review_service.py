import unittest
from src import review_service


class TestReviewService(unittest.TestCase):

    def test_retrieve_reviews(self):
        r = review_service.retrieve_reviews(42825)
        self.assertEqual(len(r), 1662)
        self.assertEqual(isinstance(r, list), True)
        print(r)
        print(type(r))


    def test_fetch_review_list(self):
        r = review_service.fetch_review_list(42825, 1)
        self.assertEqual(isinstance(r, list), True)
        self.assertEqual(len(r), 300)

#!/usr/bin/python3
""" This module is a review test module"""

import unittest
from models import base_model
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, base_model.BaseModel)


if __name__ == '__main__':
    unittest.main()

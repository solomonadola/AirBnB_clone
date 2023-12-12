#!/usr/bin/python3
""" This module is a review test module"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()

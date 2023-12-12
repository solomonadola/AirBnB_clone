#!/usr/bin/python3
""" This module is a review test module"""

import unittest
from models import base_model
from models.review import Review


class TestReview(unittest.TestCase):

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()

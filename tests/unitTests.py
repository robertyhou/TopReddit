import unittest
from flask import current_app
from app import create_app
from Parser import temp

class basicTests(unittest.TestCase):
    def subRedditCount(self):
        dict = temp(200)
        count = 0
        for item in dict:
            count += dict[item]
        self.assertTrue()


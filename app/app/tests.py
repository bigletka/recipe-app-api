"""Simple Test """

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test module"""

    def test_add_numbers(self):
        """Test adding code"""
        res=calc.add(5,6)
        self.assertEqual(res,11)    
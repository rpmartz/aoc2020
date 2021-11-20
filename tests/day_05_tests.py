from src.day_05 import halve_range

import unittest


class DayFiveTests(unittest.TestCase):

    def test_passing_bad_designator_causes_exception(self):
        with self.assertRaises(Exception):
            halve_range([], 'Q')

if __name__ == '__main__':
    unittest.main()

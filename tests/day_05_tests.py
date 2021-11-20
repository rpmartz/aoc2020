import unittest

from src.day_05 import build_row, halve_row_range, halve_column_range


class DayFiveTests(unittest.TestCase):

    def test_passing_bad_designator_causes_exception(self):
        with self.assertRaises(Exception):
            halve_row_range([], 'Q')

    def test_binary_search_for_rows(self):
        # tests case FBFBBFFRLR
        original_row = build_row(0, 128)

        first_half = halve_row_range(original_row, 'F')
        self.assertEqual(first_half, build_row(0, 64))

        second_half = halve_row_range(first_half, 'B')
        self.assertEqual(second_half, build_row(32, 64))

        third_half = halve_row_range(second_half, 'F')
        self.assertEqual(third_half, build_row(32, 48))

        fourth_partition = halve_row_range(third_half, 'B')
        self.assertEqual(fourth_partition, build_row(40, 48))

        fifth_partition = halve_row_range(fourth_partition, 'B')
        self.assertEqual(fifth_partition, build_row(44, 48))

        sixth_partition = halve_row_range(fifth_partition, 'F')
        self.assertEqual(sixth_partition, build_row(44, 46))

        seventh_partition = halve_row_range(sixth_partition, 'F')
        self.assertEqual(seventh_partition, [44])

    def test_column_binary_search(self):
        columns = build_row(0, 8)

        first_partition = halve_column_range(columns, 'R')
        self.assertEqual(first_partition, build_row(4, 8))

        second_partition = halve_column_range(first_partition, 'L')
        self.assertEqual(second_partition, build_row(4, 6))

        third_partition = halve_column_range(second_partition, 'R')
        self.assertEqual(third_partition, [5])


if __name__ == '__main__':
    unittest.main()

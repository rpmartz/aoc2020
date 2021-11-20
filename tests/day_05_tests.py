import unittest

from src.day_05 import build_row, binary_search, find_result, process_boarding_pass


class DayFiveTests(unittest.TestCase):

    def test_passing_bad_designator_causes_exception(self):
        with self.assertRaises(Exception):
            binary_search([], 'Q')

    def test_binary_search_for_rows(self):
        # tests case FBFBBFFRLR
        original_row = build_row(0, 128)

        first_half = binary_search(original_row, 'F')
        self.assertEqual(first_half, build_row(0, 64))

        second_half = binary_search(first_half, 'B')
        self.assertEqual(second_half, build_row(32, 64))

        third_half = binary_search(second_half, 'F')
        self.assertEqual(third_half, build_row(32, 48))

        fourth_partition = binary_search(third_half, 'B')
        self.assertEqual(fourth_partition, build_row(40, 48))

        fifth_partition = binary_search(fourth_partition, 'B')
        self.assertEqual(fifth_partition, build_row(44, 48))

        sixth_partition = binary_search(fifth_partition, 'F')
        self.assertEqual(sixth_partition, build_row(44, 46))

        seventh_partition = binary_search(sixth_partition, 'F')
        self.assertEqual(seventh_partition, [44])

    def test_column_binary_search(self):
        columns = build_row(0, 8)

        first_partition = binary_search(columns, 'R')
        self.assertEqual(first_partition, build_row(4, 8))

        second_partition = binary_search(first_partition, 'L')
        self.assertEqual(second_partition, build_row(4, 6))

        third_partition = binary_search(second_partition, 'R')
        self.assertEqual(third_partition, [5])

    def test_find_row_number(self):
        rows = build_row(0, 128)
        instructions = 'FBFBBFF'
        expected = 44
        actual = find_result(rows, instructions)

        self.assertEqual(expected, actual)

    def test_find_column_number(self):
        cols = build_row(0, 8)
        instructions = 'RLR'
        expected = 5
        actual = find_result(cols, instructions)

        self.assertEqual(expected, actual)

    def test_boarding_pass(self):
        self.assertEqual(567, process_boarding_pass('BFFFBBFRRR'))
        self.assertEqual(119, process_boarding_pass('FFFBBBFRRR'))
        self.assertEqual(820, process_boarding_pass('BBFFBBFRLL'))


if __name__ == '__main__':
    unittest.main()

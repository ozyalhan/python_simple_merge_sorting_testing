import unittest
import sortMergeAlgorithm as sm


# Test Cases

class TestSortMerge(unittest.TestCase):
    """Includes all test cases about sortMerge function"""

    def test_simple(self):
        """tests simple positive integers"""
        test_list = [1, 6, 3, 4, 2, -5]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = sm.merge_sort(test_list)
        self.assertEqual(expected_list, actual_list)

    def test_empty_list(self):
        """tests simple positive integers"""
        test_list = []
        expected_list = test_list.copy()
        actual_list = sm.merge_sort(test_list)
        self.assertEqual(expected_list, actual_list)

    def test_simple_negative(self):
        """tests simple negative integers"""
        test_list = [-1, -6, -3, -4, -2]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = sm.merge_sort(test_list)
        self.assertEqual(expected_list, actual_list)


if __name__ == '__main__':
    unittest.main()

from cgi import test
from sum_10_pairs import Solution
import unittest

class KnownValues(unittest.TestCase):
    known_values = (
        {
            'input': [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9],
            'case1': [[1, 9], [1, 9], [4, 6], [4, 6], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [5, 5], [6, 4], [6, 4], [9, 1], [9, 1]],
            'case2': [[1, 9], [4, 6], [5, 5], [6, 4], [9, 1]],
            'case3': [[1, 9], [4, 6], [5, 5]],
        }, 
        {
            'input': [1, 1, 5, 9, 9],
            'case1': [[1, 9], [1, 9], [1, 9], [1, 9], [9, 1], [9, 1], [9, 1], [9, 1]],
            'case2': [[1, 9], [9, 1]],
            'case3': [[1, 9]],
        },
        {
            'input': [5, 5],
            'case1': [[5, 5], [5, 5]],
            'case2': [[5, 5]],
            'case3': [[5, 5]],
        },
    )

    def test_get_sum_10_pairs_known_values(self):
        for test_case in self.known_values:
            soln = Solution(test_case['input'])
            case1 = soln.get_sum_10_pairs()
            case2 = soln.get_sum_10_pairs(duplicates=False)
            case3 = soln.get_sum_10_pairs(duplicates=False, ordered=False)
            self.assertEqual(test_case['case1'], case1)
            self.assertEqual(test_case['case2'], case2)
            self.assertEqual(test_case['case3'], case3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

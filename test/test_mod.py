import unittest


class TestSum(unittest.TestCase):
    
    def test_sum_basic(self):
        result = sum([1, 3])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
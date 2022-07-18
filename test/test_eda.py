import unittest
import pandas as pd

from utils import eda

class TestEda(unittest.TestCase):
    def test_describe_all(self):
        """
        Test that it returns the correct df description
        """
        df = pd.read_csv('test/test_data/data.csv')
        summary = eda.describe_all(df)
        self.assertEqual(summary.iloc[3]['count'], 128)
        self.assertEqual(summary.iloc[8]['unique'], 120)
        self.assertGreaterEqual(summary.iloc[1]['mean'], 30)

if __name__ == '__main__':
    unittest.main()

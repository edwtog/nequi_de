import unittest

from utils import definitions

class TestDefinitions(unittest.TestCase):
    def test_root(self):
        """
        Test that it returns the correct path
        """
        result = definitions.PRUEBA
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()

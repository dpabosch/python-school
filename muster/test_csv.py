import unittest
import muster.commons


class MyTestCase(unittest.TestCase):
    def test_read_csv(self):
        list_of_dicts = muster.commons.read_csv('probieren.csv', '../')
        self.assertNotEqual(list_of_dicts, None)


if __name__ == '__main__':
    unittest.main()

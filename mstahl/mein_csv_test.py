import unittest
import mst_csv

class MyTestCase(unittest.TestCase):
    def test_something(self):
        mst_csv.csv_import("../probieren.csv")


if __name__ == '__main__':
    unittest.main()

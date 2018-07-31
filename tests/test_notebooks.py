import os
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['notebooks']
)
IGNORE = [
    "1_DC_Flawed_Steel_Cased_Wells",
    "3_DC_Flawed_Steel_Cased_Wells_layer",
    "9_DC_Approximating_Steel_Cased_Wells_Cartesian"
]

class TestNotebooks(unittest.TestCase):

    def test_notebooks(self):
        Test = testipynb.TestNotebooks(directory=NBDIR, timeout=3600)
        self.assertTrue(Test.run_tests())

if __name__ == "__main__":
    unittest.main()

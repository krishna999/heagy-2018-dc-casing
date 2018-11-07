import os
import testipynb
import unittest
import numpy as np

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['appendix-notebooks']
)

IGNORE = ["DC_Flawed_Steel_Cased_Wells_Geologic_Noise"]

Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800, ignore=IGNORE)
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()

"""Tests for EvmGasOptimizer."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(10, 5, 100000), 0.0005, places=6)


if __name__ == "__main__":
    unittest.main()

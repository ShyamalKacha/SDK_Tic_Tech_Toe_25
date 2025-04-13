# tests/test_network_analysis.py

import unittest
from src.network_analysis import analyze_network

class TestNetworkAnalysis(unittest.TestCase):
    def test_network_insights(self):
        """Test that network insights are returned correctly."""
        result = analyze_network()
        self.assertIsInstance(result, dict)
        self.assertIn("connections", result)
        self.assertIn("suggested_connections", result)

if __name__ == "__main__":
    unittest.main()
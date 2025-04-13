# tests/test_job_market_analysis.py

import unittest
from src.job_market_analysis import analyze_job_market

class TestJobMarketAnalysis(unittest.TestCase):
    def test_job_market_insights(self):
        """Test that job market insights are generated correctly."""
        user_skills = {"Python": "Intermediate", "Data Analysis": "Beginner"}
        result = analyze_job_market(user_skills)
        self.assertIsInstance(result, dict)
        self.assertIn("Python Developer", result)
        self.assertIn("demand", result["Python Developer"])
        self.assertIn("matched_skills", result["Python Developer"])

    def test_no_matched_skills(self):
        """Test behavior when no skills match job requirements."""
        user_skills = {"Java": "Intermediate"}
        result = analyze_job_market(user_skills)
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
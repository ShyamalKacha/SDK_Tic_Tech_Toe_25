# tests/test_career_recommendations.py

import unittest
from src.career_recommendations import recommend_career_path

class TestCareerRecommendations(unittest.TestCase):
    def test_recommendations(self):
        """Test that career recommendations are generated correctly."""
        user_skills = {"Python": "Intermediate", "Data Analysis": "Beginner"}
        job_market_insights = {
            "Python Developer": {"demand": "High", "matched_skills": ["Python"]},
            "Data Analyst": {"demand": "Medium", "matched_skills": ["Data Analysis"]}
        }
        result = recommend_career_path(user_skills, job_market_insights)
        self.assertIsInstance(result, list)
        self.assertIn("Python Developer (High Demand)", result)
        self.assertIn("Data Analyst (Medium Demand)", result)

    def test_no_recommendations(self):
        """Test behavior when no recommendations are available."""
        user_skills = {}
        job_market_insights = {}
        result = recommend_career_path(user_skills, job_market_insights)
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
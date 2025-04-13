# tests/test_skills_assessment.py

import unittest
from src.skills_assessment import assess_skills

class TestSkillsAssessment(unittest.TestCase):
    def test_default_skills(self):
        """Test that default skills are returned when no input is provided."""
        result = assess_skills()
        self.assertIsInstance(result, dict)
        self.assertIn("Python", result)
        self.assertEqual(result["Python"], "Intermediate")

    def test_user_input(self):
        """Test that user-provided skills are processed correctly."""
        user_input = ["Python", "Data Science"]
        result = assess_skills(user_input)
        self.assertIsInstance(result, dict)
        self.assertIn("Python", result)
        self.assertEqual(result["Python"], "Intermediate")
        self.assertIn("Data Science", result)

if __name__ == "__main__":
    unittest.main()
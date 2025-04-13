# tests/test_resume_interview_tips.py

import unittest
from src.resume_interview_tips import get_resume_tips, get_interview_tips

class TestResumeInterviewTips(unittest.TestCase):
    def test_resume_tips(self):
        """Test that resume tips are returned as a list."""
        result = get_resume_tips()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_interview_tips(self):
        """Test that interview tips are returned as a list."""
        result = get_interview_tips()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
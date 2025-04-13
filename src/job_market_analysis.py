# src/job_market_analysis.py

import pandas as pd

def analyze_job_market(user_skills):
    """
    Analyze the job market based on user skills and current trends.
    
    Args:
        user_skills (dict): A dictionary of user skills and proficiency levels.
    
    Returns:
        dict: Insights about the job market relevant to the user's skills.
    """
    # Example job market data
    job_market_data = {
        "Python Developer": {"demand": "High", "required_skills": ["Python", "Data Analysis"]},
        "Data Analyst": {"demand": "Medium", "required_skills": ["Data Analysis", "Problem Solving"]},
        "Project Manager": {"demand": "Low", "required_skills": ["Communication", "Problem Solving"]}
    }
    
    insights = {}
    for job_title, details in job_market_data.items():
        required_skills = details["required_skills"]
        matched_skills = [skill for skill in user_skills if skill in required_skills]
        if matched_skills:
            insights[job_title] = {
                "demand": details["demand"],
                "matched_skills": matched_skills
            }
    
    return insights
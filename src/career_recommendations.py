# src/career_recommendations.py

def recommend_career_path(user_skills, job_market_insights):
    """
    Generate personalized career path recommendations based on user skills and job market insights.
    
    Args:
        user_skills (dict): A dictionary of user skills and proficiency levels.
        job_market_insights (dict): Insights about the job market relevant to the user's skills.
    
    Returns:
        list: A list of recommended career paths.
    """
    recommendations = []
    for job_title, details in job_market_insights.items():
        if details["demand"] == "High":
            recommendations.append(f"{job_title} (High Demand)")
        elif details["demand"] == "Medium":
            recommendations.append(f"{job_title} (Medium Demand)")
        else:
            recommendations.append(f"{job_title} (Low Demand)")
    
    return recommendations
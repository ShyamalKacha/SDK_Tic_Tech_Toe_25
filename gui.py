# gui.py

import tkinter as tk
from tkinter import ttk
from src.skills_assessment import assess_skills
from src.job_market_analysis import analyze_job_market
from src.resume_interview_tips import get_resume_tips, get_interview_tips
from src.career_recommendations import recommend_career_path
from src.network_analysis import analyze_network

class CareerAdvisorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent Virtual Career Advisor")
        self.root.geometry("800x600")
        self.root.configure(bg="black")  # Set the main window background to black

        # Configure custom fonts and colors
        self.custom_font = ("Helvetica", 12)
        self.bold_font = ("Helvetica", 12, "bold")
        self.text_color = "white"  # Text color for visibility on black background
        self.button_bg = "#2ecc71"  # Green button background
        self.button_fg = "white"    # White button text

        # Create notebook (tabs) with black background
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)
        style = ttk.Style()
        style.theme_use("default")  # Use a default theme for customization
        style.configure("TNotebook", background="black", borderwidth=0)
        style.configure("TNotebook.Tab", background="black", foreground="white", font=self.custom_font)
        style.map("TNotebook.Tab", background=[("selected", "#2ecc71")])  # Highlight selected tab

        # Add tabs
        self.create_skills_tab()
        self.create_job_market_tab()
        self.create_resume_interview_tab()
        self.create_career_recommendations_tab()
        self.create_network_tab()

    def create_skills_tab(self):
        tab = ttk.Frame(self.notebook, style="Black.TFrame")
        self.notebook.add(tab, text="Skills Assessment")

        # Skills input
        tk.Label(tab, text="Enter your skills (comma-separated):", font=self.custom_font, bg="black", fg=self.text_color).pack(pady=10)
        self.skills_entry = tk.Entry(tab, width=50, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        self.skills_entry.pack(pady=5)

        # Assess button
        tk.Button(tab, text="Assess Skills", command=self.assess_skills, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Result display with scrollbar
        self.skills_result = tk.Text(tab, height=10, width=60, wrap=tk.WORD, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        scrollbar = tk.Scrollbar(tab, command=self.skills_result.yview, bg="black")
        self.skills_result.config(yscrollcommand=scrollbar.set)
        self.skills_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def assess_skills(self):
        user_input = self.skills_entry.get().strip()
        if not user_input:
            self.display_message(self.skills_result, "Please enter your skills.", error=True)
            return

        user_skills = assess_skills(user_input.split(","))
        self.display_message(self.skills_result, "Your Assessed Skills:", bold=True)
        for skill, level in user_skills.items():
            self.display_message(self.skills_result, f"- {skill}: {level}")

    def create_job_market_tab(self):
        tab = ttk.Frame(self.notebook, style="Black.TFrame")
        self.notebook.add(tab, text="Job Market Analysis")

        # Job market insights button
        tk.Button(tab, text="Analyze Job Market", command=self.analyze_job_market, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Result display with scrollbar
        self.job_market_result = tk.Text(tab, height=10, width=60, wrap=tk.WORD, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        scrollbar = tk.Scrollbar(tab, command=self.job_market_result.yview, bg="black")
        self.job_market_result.config(yscrollcommand=scrollbar.set)
        self.job_market_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def analyze_job_market(self):
        user_skills = assess_skills()  # Default skills for demonstration
        job_market_insights = analyze_job_market(user_skills)
        self.display_message(self.job_market_result, "Job Market Insights:", bold=True)
        for job, details in job_market_insights.items():
            self.display_message(self.job_market_result, f"- {job}: Demand = {details['demand']}, Matched Skills = {details['matched_skills']}")

    def create_resume_interview_tab(self):
        tab = ttk.Frame(self.notebook, style="Black.TFrame")
        self.notebook.add(tab, text="Resume & Interview Tips")

        # Resume tips button
        tk.Button(tab, text="Get Resume Tips", command=self.show_resume_tips, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Interview tips button
        tk.Button(tab, text="Get Interview Tips", command=self.show_interview_tips, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Result display with scrollbar
        self.tips_result = tk.Text(tab, height=10, width=60, wrap=tk.WORD, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        scrollbar = tk.Scrollbar(tab, command=self.tips_result.yview, bg="black")
        self.tips_result.config(yscrollcommand=scrollbar.set)
        self.tips_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def show_resume_tips(self):
        resume_tips = get_resume_tips()
        self.display_message(self.tips_result, "Resume Tips:", bold=True)
        for tip in resume_tips:
            self.display_message(self.tips_result, f"- {tip}")

    def show_interview_tips(self):
        interview_tips = get_interview_tips()
        self.display_message(self.tips_result, "Interview Tips:", bold=True)
        for tip in interview_tips:
            self.display_message(self.tips_result, f"- {tip}")

    def create_career_recommendations_tab(self):
        tab = ttk.Frame(self.notebook, style="Black.TFrame")
        self.notebook.add(tab, text="Career Recommendations")

        # Generate recommendations button
        tk.Button(tab, text="Generate Recommendations", command=self.generate_recommendations, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Result display with scrollbar
        self.recommendations_result = tk.Text(tab, height=10, width=60, wrap=tk.WORD, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        scrollbar = tk.Scrollbar(tab, command=self.recommendations_result.yview, bg="black")
        self.recommendations_result.config(yscrollcommand=scrollbar.set)
        self.recommendations_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def generate_recommendations(self):
        user_skills = assess_skills()  # Default skills for demonstration
        job_market_insights = analyze_job_market(user_skills)
        recommendations = recommend_career_path(user_skills, job_market_insights)
        self.display_message(self.recommendations_result, "Career Recommendations:", bold=True)
        for recommendation in recommendations:
            self.display_message(self.recommendations_result, f"- {recommendation}")

    def create_network_tab(self):
        tab = ttk.Frame(self.notebook, style="Black.TFrame")
        self.notebook.add(tab, text="Network Analysis")

        # Analyze network button
        tk.Button(tab, text="Analyze Network", command=self.analyze_network, font=self.custom_font, bg=self.button_bg, fg=self.button_fg).pack(pady=10)

        # Result display with scrollbar
        self.network_result = tk.Text(tab, height=10, width=60, wrap=tk.WORD, font=self.custom_font, bg="#333", fg=self.text_color, insertbackground="white")
        scrollbar = tk.Scrollbar(tab, command=self.network_result.yview, bg="black")
        self.network_result.config(yscrollcommand=scrollbar.set)
        self.network_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def analyze_network(self):
        network_insights = analyze_network()
        self.display_message(self.network_result, "Network Insights:", bold=True)
        self.display_message(self.network_result, f"- Connections: {network_insights['connections']}")
        self.display_message(self.network_result, f"- Suggested Connections: {network_insights['suggested_connections']}")

    def display_message(self, text_widget, message, bold=False, error=False):
        """
        Display a message in the given Text widget with optional formatting.
        
        Args:
            text_widget (tk.Text): The Text widget where the message will be displayed.
            message (str): The message to display.
            bold (bool): Whether to display the message in bold.
            error (bool): Whether to display the message as an error (red text).
        """
        tag = None
        if bold:
            tag = "bold"
            text_widget.tag_configure("bold", font=self.bold_font, foreground=self.text_color)
        if error:
            tag = "error"
            text_widget.tag_configure("error", foreground="red")

        text_widget.insert(tk.END, message + "\n", tag)


if __name__ == "__main__":
    root = tk.Tk()
    app = CareerAdvisorApp(root)
    root.mainloop()
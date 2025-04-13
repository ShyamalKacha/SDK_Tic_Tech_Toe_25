# main.py

import tkinter as tk
from gui import CareerAdvisorApp

def main():
    """
    Entry point of the application.
    Initializes and runs the GUI for the Intelligent Virtual Career Advisor.
    """
    # Create the root Tkinter window
    root = tk.Tk()
    
    # Set up the application title and size
    root.title("Intelligent Virtual Career Advisor")
    root.geometry("800x600")  # Width x Height
    
    # Initialize the CareerAdvisorApp GUI
    app = CareerAdvisorApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
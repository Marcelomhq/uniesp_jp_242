import tkinter as tk
from tkinter import messagebox

def start_scraping():
    messagebox.showinfo("Scraping", "Starting the scraping process!")

def show_saved_advices():
    messagebox.showinfo("Saved Advices", "Displaying saved advices!")

def exit_app():
    app.destroy()

# Create the main window
app = tk.Tk()
app.title("Advice Scraper")
app.geometry("300x200")  # Set window size

# Create buttons for the menu
tk.Label(app, text="Welcome to Advice Scraper!", font=("Arial", 16)).pack(pady=10)
tk.Button(app, text="1. Start Scraping", command=start_scraping).pack(pady=5)
tk.Button(app, text="2. Show Saved Advices", command=show_saved_advices).pack(pady=5)
tk.Button(app, text="3. Exit", command=exit_app).pack(pady=5)

# Run the GUI loop
app.mainloop()
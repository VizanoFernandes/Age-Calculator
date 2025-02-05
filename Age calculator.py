import tkinter as tk
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        year = year_entry.get()
        month = month_entry.get()
        day = day_entry.get()

        if not name or not year or not month or not day:
            result_label.config(text="Please fill in all fields.")
            root.geometry("400x350")  # Adjust UI size
            return

        year = int(year)
        month = int(month)
        day = int(day)

        today = date.today()
        birth_date = date(year, month, day)

        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day

        if age_days < 0:
            age_days += (birth_date.replace(month=birth_date.month + 1, day=1) - birth_date).days
            age_months -= 1

        if age_months < 0:
            age_months += 12
            age_years -= 1

        result_label.config(text=f"Hello {name}, you are {age_years} years, {age_months} months, and {age_days} days old.")
        root.geometry("500x400")  # Expand UI for the message
    except ValueError:
        result_label.config(text="Please enter valid numbers for year, month, and day.")
        root.geometry("400x350")  # Adjust UI size
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")
        root.geometry("400x350")  # Adjust UI size

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Name Label and Entry
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Year Label and Entry
year_label = tk.Label(root, text="Enter Your Birth Year:")
year_label.pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

# Month Label and Entry
month_label = tk.Label(root, text="Enter Your Birth Month:")
month_label.pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

# Day Label and Entry
day_label = tk.Label(root, text="Enter Your Birth Day:")
day_label.pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", fg="blue", wraplength=480, justify="center")
result_label.pack(pady=(10, 0))

# Run the application
root.mainloop()

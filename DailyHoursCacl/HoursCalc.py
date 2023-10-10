import tkinter as tk
from datetime import datetime

def calculate():
    # Get start and end times
    start_time = datetime.strptime(start_var.get(), "%H:%M")
    end_time = datetime.strptime(end_var.get(), "%H:%M")
    
    # Calculate hours worked
    delta = end_time - start_time
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60
    worked_hours = hours + minutes/60

    # Expected hours
    expected_hours = 7.0
    rahmz = min(worked_hours, expected_hours)
    glz = worked_hours - expected_hours

    # Set results
    results.delete(1.0, tk.END)
    results.insert(tk.END, f"Datum: {datetime.now().strftime('%d.%m.%Y')}\n")
    results.insert(tk.END, f"Tag: {datetime.now().strftime('%A')}\n")
    results.insert(tk.END, f"Beschreibung zum Tag: Default Description\n")
    results.insert(tk.END, f"von: {start_var.get()}\n")
    results.insert(tk.END, f"bis: {end_var.get()}\n")
    results.insert(tk.END, f"Std.: {hours},{minutes:02}\n")
    results.insert(tk.END, f"Sollz: {expected_hours:0.2f}\n")
    results.insert(tk.END, f"Rahmz: {rahmz:0.2f}\n")
    results.insert(tk.END, f"Glz: {glz:0.2f}\n")
    results.insert(tk.END, f"Mehrz: {glz:0.2f}\n") # This is an assumption
    results.insert(tk.END, f"TAZP: Default Value\n")

root = tk.Tk()
root.title("Time Calculator")

# Variables
start_var = tk.StringVar()
end_var = tk.StringVar()

# Input fields and labels
tk.Label(root, text="Start time (HH:MM)").pack(pady=10)
tk.Entry(root, textvariable=start_var).pack()

tk.Label(root, text="End time (HH:MM)").pack(pady=10)
tk.Entry(root, textvariable=end_var).pack()

# Button to perform calculation
tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

# Results display
results = tk.Text(root, height=15, width=50)
results.pack(pady=10)

root.mainloop()

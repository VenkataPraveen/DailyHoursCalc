import tkinter as tk
from datetime import datetime

def calc_pause(slot_hours):
    pause_after_six_hours = 0.5
    pause_after_nine_hours = 0.75

    if slot_hours > 9 + pause_after_nine_hours:
        slot_hours -= pause_after_nine_hours
    elif slot_hours >= 9:
        slot_hours = 9
    elif slot_hours > 6 + pause_after_six_hours:
        slot_hours -= pause_after_six_hours
    elif slot_hours >= 6:
        slot_hours = 6

    return slot_hours

def calculate():
    start_time = datetime.strptime(start_var.get(), "%H:%M")
    end_time = datetime.strptime(end_var.get(), "%H:%M")
    
    # Calculate hours worked
    delta = end_time - start_time
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60
    worked_hours = hours + minutes/60

    rahmz = calc_pause(worked_hours)
    glz = worked_hours - rahmz

    # Set results
    results.delete(1.0, tk.END)
    results.insert(tk.END, f"Datum: {datetime.now().strftime('%d.%m.%Y')}\n")
    results.insert(tk.END, f"Tag: {datetime.now().strftime('%A')}\n")
    results.insert(tk.END, f"Beschreibung zum Tag: Default Description\n")
    results.insert(tk.END, f"von: {start_var.get()}\n")
    results.insert(tk.END, f"bis: {end_var.get()}\n")
    results.insert(tk.END, f"Std.: {worked_hours:.2f}\n")
    results.insert(tk.END, f"Sollz: 7.00\n")
    results.insert(tk.END, f"Rahmz: {rahmz:.2f}\n")
    results.insert(tk.END, f"Glz: {glz:.2f}\n")
    results.insert(tk.END, f"Mehrz: {glz:.2f}\n") # Assuming Mehrz is same as Glz
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

# pip install numpy matplotlib tkinter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

def run_simulation(params):

    mj_kg = params['mj_kg']
    initial_mass = params['initial_mass']
    fuel_mass = params['fuel_mass']
    fuel_burn_rate = params['fuel_burn_rate']
    exhaust_velocity = params['exhaust_velocity']
    sim_time = params['sim_time']


    G = 6.674e-11
    mass_earth = 5.972e24
    earth_radius = 3963.19 * 1609.34
    surface_g = G * mass_earth / earth_radius**2

    dt = 0.1
    time = np.arange(0, sim_time + dt, dt)

    solid_mass = initial_mass - fuel_mass

    burn_time = fuel_mass / fuel_burn_rate
    thrust_force = fuel_burn_rate * exhaust_velocity



    # Initial conditions
    height = 0
    velocity = 0
    apogee_height = None
    exit_atmo = False

    velocity_list = []
    height_list = []

    for t in time:
        g = G * mass_earth / (earth_radius + height)**2

        if fuel_mass > 0:
            fuel_mass -= fuel_burn_rate * dt
            fuel_mass = max(fuel_mass, 0)

        rocket_mass = solid_mass + fuel_mass
        weight = rocket_mass * g
        thrust = thrust_force if fuel_mass > 0 else 0

        acceleration = (thrust - weight) / rocket_mass
        velocity += acceleration * dt
        height += velocity * dt

        velocity_list.append(velocity)
        height_list.append(height)

        if height >= 100_000 and not exit_atmo:
            exit_atmo = True
        if velocity < 0 and apogee_height is None:
            apogee_height = height
        if apogee_height is not None and height <= 0:
            height = 0
            break

    time_truncated = time[:len(height_list)]

    return {
        "time": time_truncated,
        "height": height_list,
        "velocity": velocity_list,
        "apogee": apogee_height,
        "exit_atmo": exit_atmo,
        "force_required": initial_mass * surface_g,
    }


def start_simulation():
    try:
        params = {
            "mj_kg": float(entry_mj_kg.get()),
            "initial_mass": float(entry_mass.get()),
            "fuel_mass": float(entry_fuel_mass.get()),
            "fuel_burn_rate": float(entry_burn_rate.get()),
            "exhaust_velocity": float(entry_exhaust_velocity.get()),
            "sim_time": float(entry_sim_time.get()),
        }
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    results = run_simulation(params)

    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax1.plot(results["time"], results["height"], color="blue", label="Height (m)")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Height (m)", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(results["time"], results["velocity"], color="red", label="Velocity (m/s)")
    ax2.set_ylabel("Velocity (m/s)", color="red")
    ax2.tick_params(axis="y", labelcolor="red")

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    plt.title("Rocket Launch Simulation")

    for widget in frame_plot.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    result_text = (
        f"Apogee: {results['apogee']:.1f} m\n"
        f"Exited Atmosphere: {results['exit_atmo']}\n"
        f"Force Required for Liftoff: {results['force_required']:.1f} N"
    )
    lbl_results.config(text=result_text)


root = tk.Tk()
root.title("Rocket Simulation")
root.geometry("900x700")

frame_inputs = ttk.Frame(root, padding=10)
frame_inputs.pack(side=tk.TOP, fill=tk.X)

labels = [
    ("Energy Density (MJ/kg):", "140"),
    ("Rocket Mass (kg):", "20000"),
    ("Fuel Mass (kg):", "700"),
    ("Fuel Burn Rate (kg/s):", "100"),
    ("Exhaust Velocity (m/s):", "3000"),
    ("Simulation Time (s):", "1200"),
]
entries = []

for i, (label_text, default) in enumerate(labels):
    ttk.Label(frame_inputs, text=label_text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=3)
    e = ttk.Entry(frame_inputs)
    e.insert(0, default)
    e.grid(row=i, column=1, padx=5, pady=3)
    entries.append(e)

(entry_mj_kg, entry_mass, entry_fuel_mass, entry_burn_rate, entry_exhaust_velocity, entry_sim_time) = entries

ttk.Button(frame_inputs, text="Run Simulation", command=start_simulation).grid(row=0, column=2, rowspan=2, padx=10)

lbl_results = ttk.Label(frame_inputs, text="", font=("Arial", 11), foreground="blue")
lbl_results.grid(row=6, column=0, columnspan=3, pady=10)

frame_plot = ttk.Frame(root)
frame_plot.pack(fill=tk.BOTH, expand=True)

root.mainloop()

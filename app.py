"""
Porsche 911 Braking Physics Simulation
Prepared by: Talia Fouda
Grade 12 Physics — Car Braking

Educational model only. Example values are assumptions, not measured Porsche test data.
Run with: python Talia_Fouda_Porsche_911_Braking_Simulation.py
Requires: matplotlib (install with: python -m pip install matplotlib)
"""
import math
import matplotlib.pyplot as plt

G = 9.81  # gravitational acceleration, m/s^2
REACTION_TIME = 1.5  # seconds; illustrative assumption

def stopping_distances(speed_kmh, friction, reaction_time=REACTION_TIME):
    """Return reaction, braking, and total stopping distances in metres."""
    if speed_kmh < 0:
        raise ValueError("Speed cannot be negative.")
    if friction <= 0:
        raise ValueError("Friction coefficient must be greater than zero.")
    if reaction_time < 0:
        raise ValueError("Reaction time cannot be negative.")

    speed_ms = speed_kmh / 3.6
    reaction_distance = speed_ms * reaction_time
    deceleration = friction * G
    braking_distance = (speed_ms ** 2) / (2 * deceleration)
    total_distance = reaction_distance + braking_distance
    return reaction_distance, braking_distance, total_distance

def print_table():
    speeds = [50, 80, 100, 120]
    friction = 0.80
    print("\\nPORSCHE 911 BRAKING MODEL")
    print("Assumptions: reaction time = 1.5 s, friction = 0.80, level road")
    print(f"{'Speed':>8} {'Reaction (m)':>15} {'Braking (m)':>14} {'Total (m)':>12}")
    for speed in speeds:
        reaction, braking, total = stopping_distances(speed, friction)
        print(f"{speed:>7}  {reaction:>13.1f}  {braking:>12.1f}  {total:>10.1f}")

def plot_speed_comparison():
    speeds = list(range(20, 131, 10))
    friction_values = [0.80, 0.40, 0.20]
    labels = {
        0.80: "Higher grip (μ=0.80)",
        0.40: "Reduced grip (μ=0.40)",
        0.20: "Very low grip (μ=0.20)"
    }
    for friction in friction_values:
        totals = [stopping_distances(speed, friction)[2] for speed in speeds]
        plt.plot(speeds, totals, marker="o", label=labels[friction])
    plt.title("Estimated Porsche 911 Stopping Distance")
    plt.xlabel("Starting speed (km/h)")
    plt.ylabel("Total stopping distance (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("porsche_911_stopping_distance.png", dpi=200)
    plt.show()

def main():
    print_table()
    plot_speed_comparison()

if _name_ == "_main_":
    main()

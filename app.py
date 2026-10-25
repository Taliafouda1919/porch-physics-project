import streamlit as st
import matplotlib.pyplot as plt

# Porsche 911 Braking Physics Simulation
# Prepared by: Talia Fouda
# Grade 12 Physics Project

G = 9.81
REACTION_TIME = 1.5

# Configure the Streamlit page
st.set_page_config(
    page_title="Porsche 911 Braking Simulation",
    page_icon="​￼​",
    layout="wide"
)


def stopping_distances(speed_kmh, friction, reaction_time=REACTION_TIME):
    """Calculate reaction, braking, and total stopping distances."""

    if speed_kmh < 0:
        raise ValueError("Speed cannot be negative.")

    if friction <= 0:
        raise ValueError("Friction must be greater than zero.")

    if reaction_time < 0:
        raise ValueError("Reaction time cannot be negative.")

    speed_ms = speed_kmh / 3.6
    reaction_distance = speed_ms * reaction_time
    deceleration = friction * G
    braking_distance = speed_ms ** 2 / (2 * deceleration)
    total_distance = reaction_distance + braking_distance

    return reaction_distance, braking_distance, total_distance


# Page heading
st.title("Porsche 911 Braking Physics Simulation")
st.subheader("Prepared by: Talia Fouda")
st.write("Grade 12 Physics - Car Braking")

st.info(
    "Educational model only. The reaction time and friction "
    "values are assumptions, not measured Porsche test data."
)

# User controls
st.header("1. Simulation Settings")

col1, col2 = st.columns(2)

with col1:
    speed = st.slider(
        "Starting Speed (km/h)",
        min_value=0,
        max_value=300,
        value=100,
        step=10
    )

with col2:
    friction = st.slider(
        "Road Friction Coefficient (mu)",
        min_value=0.10,
        max_value=1.00,
        value=0.80,
        step=0.05,
        format="%.2f"
    )

# Calculate results
reaction, braking, total = stopping_distances(
    speed, friction
)

# Display calculated results
st.header("2. Stopping Distance Results")

col1, col2, col3 = st.columns(3)

col1.metric("Reaction Distance", f"{reaction:.2f} m")
col2.metric("Braking Distance", f"{braking:.2f} m")
col3.metric("Total Stopping Distance", f"{total:.2f} m")

st.caption(
    "Assumptions: reaction time = 1.5 seconds, "
    "gravitational acceleration = 9.81 m/s², level road."
)

# Graph
st.header("3. Effect of Speed and Road Grip")

speeds = list(range(0, 301, 10))

friction_values = [0.80, 0.40, 0.20]

labels = {
    0.80: "Higher grip (mu = 0.80)",
    0.40: "Reduced grip (mu = 0.40)",
    0.20: "Very low grip (mu = 0.20)"
}

fig, ax = plt.subplots(figsize=(10, 5))

for mu in friction_values:
    distances = [
        stopping_distances(v, mu)[2]
        for v in speeds
    ]

    ax.plot(
        speeds,
        distances,
        marker="o",
        markersize=3,
        label=labels[mu]
    )

ax.set_title("Estimated Porsche 911 Total Stopping Distance")
ax.set_xlabel("Starting Speed (km/h)")
ax.set_ylabel("Total Stopping Distance (m)")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Results table
st.header("4. Stopping Distance Table")

table_data = []

for v in [50, 80, 100, 120]:
    r, b, t = stopping_distances(v, friction)

    table_data.append({
        "Speed (km/h)": v,
        "Reaction Distance (m)": round(r, 2),
        "Braking Distance (m)": round(b, 2),
        "Total Distance (m)": round(t, 2)
    })

st.dataframe(
    table_data,
    use_container_width=True,
    hide_index=True
)

# Physics formulas
st.header("5. Physics Formulas")

st.latex(r"v = \frac{\text{speed in km/h}}{3.6}")
st.latex(r"d_r = vt")
st.latex(r"d_b = \frac{v^2}{2\mu g}")
st.latex(r"d_{\text{total}} = d_r + d_b")

st.write("Where:")
st.write("- v = speed in metres per second")
st.write("- t = driver's reaction time in seconds")
st.write("- mu = coefficient of friction")
st.write("- g = gravitational acceleration (9.81 m/s²)")
st.write("- d_r = reaction distance")
st.write("- d_b = braking distance")

# Conclusion
st.header("6. Conclusion")

st.write(
    "The simulation shows that stopping distance increases "
    "as speed increases. Lower road friction also increases "
    "braking distance. This happens because braking distance "
    "depends on the square of speed and inversely on friction."
)

st.warning(
    "This is a simplified physics model. It does not include "
    "aerodynamic drag, road slope, changing tire grip, or the "
    "detailed behaviour of the braking system. Results are "
    "estimates, not verified Porsche performance measurements."
)

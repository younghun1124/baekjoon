import numpy as np
from scipy.optimize import fsolve

def calculate_time_and_speed(m_p, r_crank, h_pedal, gear_ratio, r_wheel):
    m_total = m_p + 1  # Total mass (person + bicycle)
    F_pedal = m_p * g  # Force applied to pedal
    C_rr = 0.015  # Rolling resistance coefficient
    C_d = 1.0  # Drag coefficient
    A = 1.0  # Frontal area (m^2)
    rho = 1.225  # Air density (kg/m^3)

    # Initialize simulation parameters
    dt = 0.01  # Time step (s)
    t = 0  # Total time
    v_pedal = 0  # Initial pedal speed
    h_moved = 0  # Total pedal displacement

    # Simulate pedal motion until the pedal depth is reached
    while h_moved < h_pedal:
        # Rolling resistance
        F_rolling = C_rr * m_total * g

        # Air resistance (negligible for pedal speed)
        F_drag = 0  # Optional: Include if needed

        # Total resistance
        F_resistance = F_rolling + F_drag

        # Pedal acceleration
        m_pedal = 0.1  # Approximate equivalent mass of pedal system
        a_pedal = (F_pedal - F_resistance) / m_pedal

        # Update pedal speed and position
        v_pedal += a_pedal * dt
        h_moved += v_pedal * dt
        t += dt

    print(f"Time to press the pedal: {t:.6f} seconds")

    # Work done by the pedal
    W_pedal = F_pedal * h_pedal

    # Distance traveled during the pedal stroke
    theta_crank = np.arccos(1 - h_pedal / r_crank)
    theta_wheel = theta_crank * gear_ratio
    s = r_wheel * theta_wheel  # Distance traveled by the wheel

    # Residual function for final speed
    def residual(v):
        F_drag = 0.5 * rho * v**2 * C_d * A  # Air resistance
        F_resistance = F_rolling + F_drag
        W_resistance = F_resistance * s
        KE = 0.5 * m_total * v**2
        return W_pedal - W_resistance - KE

    # Solve for final speed
    v_guess = 5  # Initial guess
    v_solution = fsolve(residual, v_guess)
    v_final = v_solution[0]

    print(f"Final Speed Achieved: {v_final:.6f} m/s")

# Example inputs
m_p = 70  # Person's mass (kg)
r_crank = 0.17  # Crank length (m)
h_pedal = 0.2  # Pedal depth (m)
gear_ratio = 10.0  # Gear ratio
r_wheel = 0.35  # Wheel radius (m)
g=9.8
calculate_time_and_speed(m_p, r_crank, h_pedal, gear_ratio, r_wheel)

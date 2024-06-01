import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# System parameters
omega_n = 1  # Natural frequency (rad/s)
zeta_values = [0.5, 1, 1.5]  # Damping ratios for underdamped, critically damped, overdamped
labels = ['Underdamped (ζ=0.5)', 'Critically Damped (ζ=1)', 'Overdamped (ζ=1.5)']

plt.figure(figsize=(10, 6))

# Simulate step response for each damping ratio
for zeta, label in zip(zeta_values, labels):
    # Define the second-order system transfer function
    num = [omega_n**2]
    den = [1, 2*zeta*omega_n, omega_n**2]
    system_tf = ctl.tf(num, den)
    
    # Simulate step response
    t, y = ctl.step_response(system_tf)
    
    # Plot
    plt.plot(t, y, label=label)

# Enhancements for the plot
plt.title('Step Response for Different Damping Ratios')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.grid(True)
plt.legend()
plt.show()

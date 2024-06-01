import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Define the plant transfer function
tau = 1  # Time constant of the plant
plant_tf = ctl.tf([1], [tau, 1])  # Plant transfer function G(s) = 1 / (tau*s + 1)

# Ranges for Kp and Ki
Kp_range = np.linspace(0, 100, 20)  # 20 points from 0 to 100 for Kp
Ki_range = np.linspace(0, 4500, 20)  # 20 points from 0 to 4500 for Ki

# Prepare the meshgrid for Kp and Ki
Kp_grid, Ki_grid = np.meshgrid(Kp_range, Ki_range)
overshoot_grid = np.zeros(Kp_grid.shape)

# Function to calculate percent overshoot
def calculate_overshoot(response):
    peak = np.max(response)
    steady_state = response[-1]
    overshoot = (peak - steady_state) / steady_state * 100
    return overshoot

# Calculate percent overshoot for each (Kp, Ki) pair
for i in range(len(Ki_range)):
    for j in range(len(Kp_range)):
        Kp = Kp_grid[i, j]
        Ki = Ki_grid[i, j]
        PI_tf = ctl.tf([Kp, Ki], [1, 0])
        closed_loop_tf = ctl.feedback(PI_tf * plant_tf)
        _, response = ctl.step_response(closed_loop_tf)
        overshoot_grid[i, j] = calculate_overshoot(response)

# Plotting the heatmap of percent overshoot
plt.figure(figsize=(10, 8))
contour = plt.contourf(Kp_grid, Ki_grid, overshoot_grid, cmap='viridis', levels=np.linspace(0, 100, 11))
plt.colorbar(contour, label='Percent Overshoot')
plt.title('Percent Overshoot for Varying Kp and Ki')
plt.xlabel('Kp')
plt.ylabel('Ki')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant parameters
tau = 1  # 플랜트의 time constant
plant_tf = ctl.tf([1], [tau, 1])  # 플랜트 전달함수

# Simulation parameters
t = np.linspace(0, 10, 1000)
Ki_fixed = 1  # ki는 고정
Kp_values = [0.5, 1, 2, 4]  # kp 가변

plt.figure(figsize=(12, 6))

for Kp in Kp_values:
    # PI controller 전달함수
    PI_tf = ctl.tf([Kp, Ki_fixed], [1, 0])
    
    # 폐루프 전달함수
    closed_loop_tf = ctl.feedback(PI_tf * plant_tf)
    
    # Step response
    t, y = ctl.step_response(closed_loop_tf, t)

    plt.plot(t, y, label=f'Kp={Kp}, Ki={Ki_fixed}')

plt.title('Step Response (kp varying / ki fixed)')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant parameters
tau = 1  # 플랜트의 time constant

# 플랜트 전달함수 G(s) = 1 / (tau*s)
plant_tf = ctl.tf([1], [tau, 0])

ts = 0.1
zeta_value = [0.1, 0.5, 1/(2**(1/2)), 1, 1.5]
Kp_value = 9.2/ts

# 스텝 응답을 그리기 위한 준비
plt.figure(figsize=(8, 6))

# ζ값에 따라 for문 반복
for zeta in zeta_value:
    wn_value = Kp_value/(2*zeta)
    Ti_value = (2*zeta)/wn_value
    Ki_value = Kp_value/Ti_value
    
    # PI controller 전달함수 Gc(s) = Kp + Ki/s
    PI_tf = ctl.tf([Kp_value, Ki_value], [1, 0])    
    
    # 폐루프 전달함수 계산 Gcl(s) = Gc(s)*G(s) / (1 + Gc(s)*G(s))
    closed_loop_tf = ctl.feedback(PI_tf * plant_tf)
    
    # 시간 벡터 및 스텝 응답 계산
    time = np.linspace(0, 0.35, 1000)
    time, response = ctl.step_response(closed_loop_tf, time)
    
    # 스텝 응답 플롯
    plt.plot(time, response, label=f'ζ={zeta}, Kp={Kp_value:.2f}, Ki={Ki_value:.2f}')

# 플롯 서식 지정
plt.title('Step Response of Closed-Loop Systems')
plt.xlabel('Time (seconds)')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.show()


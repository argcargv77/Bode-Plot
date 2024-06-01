import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant parameters
tau = 1  # 플랜트 time constant

# 플랜트 전달함수 G(s) = 1 / (tau*s + 1)
plant_tf = ctl.tf([1], [tau, 1])

t = np.linspace(0, 10, 1000)

# PI controller 파라미터
Ki_fixed = 4232.03  # ki 고정
Kp_values = [80, 92, 100, 110]  # kp 가변

plt.figure(figsize=(14, 10))

# kp값 반복하며 for문
for Kp in Kp_values:
    # PI controller 전달함수 Gc(s) = Kp + Ki/s
    PI_tf = ctl.tf([Kp, Ki_fixed], [1, 0])
    
    # 폐루프 전달함수 계산 Gcl(s) = Gc(s)*G(s) / (1 + Gc(s)*G(s))
    closed_loop_tf = ctl.feedback(PI_tf * plant_tf)  
    
    # 폐루프 시스템 보드플랏 생성
    mag, phase, omega = ctl.bode(closed_loop_tf, dB=True, Plot=False)
    
    # magnitude response
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, 20*np.log10(mag), label=f'Kp={Kp}, Ki={Ki_fixed}')
    plt.title('bode plot: Magnitude Response (Ki fixed)')
    plt.ylabel('Magnitude (dB)')
    
    # phase response
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, np.degrees(phase), label=f'Kp={Kp}, Ki={Ki_fixed}')
    plt.title('bode plot: Phase Response (Ki fixed)')
    plt.xlabel('Frequency (rad/sec)')
    plt.ylabel('Phase (degrees)')

plt.legend()
plt.tight_layout()
plt.show()


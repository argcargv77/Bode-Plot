import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant parameters
tau = 1  # 플랜트의 time constant

# 플랜트 전달함수 G(s) = 1 / (tau*s + 1)
plant_tf = ctl.tf([1], [tau, 1])

t = np.linspace(0, 10, 1000)

# PI controller 파라미터
Kp_fixed = 92  # kp 고정
Ki_values = [2000, 4232.03, 6000]  # ki 가변

plt.figure(figsize=(14, 10))

# ki값 반복하며 for문
for Ki in Ki_values:
    # PI controller 전달함수 Gc(s) = Kp + Ki/s
    PI_tf = ctl.tf([Kp_fixed, Ki], [1, 0])
    
    # 폐루프 전달함수 계산 Gcl(s) = Gc(s)*G(s) / (1 + Gc(s)*G(s))
    closed_loop_tf = ctl.feedback(PI_tf * plant_tf)
    
    # 폐루프 시스템 보드플랏 생성
    mag, phase, omega = ctl.bode(closed_loop_tf, dB=True, Plot=False)

    # magnitude response
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, 20 * np.log10(mag), label=f'Ki={Ki}, Kp={Kp_fixed}')
    plt.ylabel('Magnitude (dB)')
    plt.title('bode plot: Magnitude Response (Kp fixed)')

    # phase response
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, np.degrees(phase), label=f'Ki={Ki}, Kp={Kp_fixed}')
    plt.title('bode plot: Phase Response (Kp fixed)')
    plt.xlabel('Frequency (rad/sec)')
    plt.ylabel('Phase (degrees)')

plt.legend()
plt.tight_layout()
plt.show()


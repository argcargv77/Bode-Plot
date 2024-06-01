import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant parameters
tau = 1  # 플랜트의 time constant

# 플랜트 전달함수 G(s) = 1 / (tau*s)
plant_tf = ctl.tf([1], [tau, 0])

ts=0.1
zeta_value = [0.1, 0.5, 1/(2**(1/2)), 1, 1.5]
Kp_value = 9.2/ts

# 서브플롯 준비
plt.figure(figsize=(10, 8))
mag_plot = plt.subplot(2, 1, 1)
phase_plot = plt.subplot(2, 1, 2)

# ζ값에 따라 for문 반복
for zeta in zeta_value:
    wn_value = Kp_value/(2*zeta)
    Ti_value = (2*zeta)/wn_value
    Ki_value = Kp_value/Ti_value
    
    # PI controller 전달함수 Gc(s) = Kp + Ki/s
    PI_tf = ctl.tf([Kp_value, Ki_value], [1, 0])    
    
    # 폐루프 전달함수 계산 Gcl(s) = Gc(s)*G(s) / (1 + Gc(s)*G(s))
    closed_loop_tf = ctl.feedback(PI_tf * plant_tf)
    
    # 폐루프 시스템 보드플랏 생성
    mag, phase, omega = ctl.bode(closed_loop_tf, dB=True, Plot=False)
    
    # magnitude response
    mag_plot.semilogx(omega, 20 * np.log10(mag), label=f'ζ={zeta}, Kp={Kp_value:.2f}, Ki={Ki_value:.2f}')
    
    # phase response
    phase_plot.semilogx(omega, np.degrees(phase), label=f'ζ={zeta}, Kp={Kp_value:.2f}, Ki={Ki_value:.2f}')

# 서브플롯 포맷팅 및 레이블
mag_plot.set_ylabel('Magnitude (dB)')
mag_plot.set_title('Bode Plot: Magnitude Response')
mag_plot.legend()

phase_plot.set_title('Bode Plot: Phase Response')
phase_plot.set_xlabel('Frequency (rad/sec)')
phase_plot.set_ylabel('Phase (degrees)')
phase_plot.legend()

plt.tight_layout()
plt.show()

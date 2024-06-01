import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
Kp = np.linspace(1, 100, 100)
ts = 9.2 / Kp

plt.figure(1)
plt.plot(Kp, ts, label='ts vs Kp')

plt.title('Settling Time(ts) VS Proportional Gain(Kp)')
plt.xlabel('Proportional Gain(Kp)')
plt.ylabel('Settling Time(ts)')

plt.legend()
plt.grid(True)
plt.show()

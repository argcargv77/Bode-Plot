import control as ct
import numpy as np
import matplotlib.pyplot as plt

zeta = 1/np.sqrt(2) # 1/root(2)
wn = 2*np.pi*50 # 50Hz
ts = 0.1 

# Parameters
Kp = 80
Ki = 2*Kp / ts * zeta **2
Ti = Kp/Ki

# Plant
num1 = [1]
den1 = [1, 0]
G = ct.tf(num1, den1)
print("G = ", G)

# PI Controller
num2 = [Kp*Ti, Kp]
den2 = [Ti]
Gc = ct.tf(num2, den2)
print("Gc = ", Gc)

# Open-loop T.F
open_tf = Gc * G
print("Open-loop T.F = ", open_tf)

# closed-loop T.F
closed_tf = open_tf /(1 + open_tf)
print("Closed-loop T.F = ", closed_tf)


# pole-zero map 
plt.figure(1)
ct.pzmap(closed_tf)

# Bode-plot
plt.figure(2)
ct.bode_plot(Gc)
plt.figure(3)
ct.bode_plot(closed_tf)

# Root-locus
plt.figure(4)
ct.root_locus(closed_tf)
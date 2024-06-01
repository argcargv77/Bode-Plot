import control as ct
import numpy as np
import matplotlib.pyplot as plt


wn = 50.0
zeta1 = 1.0
zeta2 = 0.9
zeta3 = 0.8
zeta4 = 1/np.sqrt(2) # 1/root(2)
zeta5 = 0.6
zeta5 = 0.5
zeta5 = 0.4
zeta6 = 0.3

# zeta = 1
num = [wn**2]
den1 = [1, 2*zeta1*wn, wn**2]
system1 = ct.tf(num, den1)

# zeta = 0.9
den2 = [1, 2*zeta2*wn, wn**2]
system2 = ct.tf(num, den2)

# zeta = 0.8
den3 = [1, 2*zeta3*wn, wn**2]
system3 = ct.tf(num, den3)

# zeta = 1/root(2)
den3 = [1, 2*zeta4*wn, wn**2]
system4 = ct.tf(num, den3)

# zeta = 0.6
den3 = [1, 2*zeta5*wn, wn**2]
system5 = ct.tf(num, den3)

# zeta = 0.5
den3 = [1, 2*zeta6*wn, wn**2]
system6 = ct.tf(num, den3)

# zeta = 0.4
den3 = [1, 2*zeta6*wn, wn**2]
system7 = ct.tf(num, den3)

# zeta = 0.3
den3 = [1, 2*zeta6*wn, wn**2]
system8 = ct.tf(num, den3)

plt.figure(1)
ct.bode(system1, Hz=True)
ct.bode(system2, Hz=True)
ct.bode(system3, Hz=True)
ct.bode(system4, Hz=True)
ct.bode(system5, Hz=True)
ct.bode(system6, Hz=True)
ct.bode(system7, Hz=True)
ct.bode(system8, Hz=True)


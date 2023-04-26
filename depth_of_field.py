# depth_of_field.py
# Max Liang
# created 04/25/23
# Descrption:
#
#


import numpy as np
import matplotlib.pyplot as plt


const = 1
a, b, c, d = 16, 0.004, 275, 5


def dof(A=a*const, d=b*const, s_0=c*const, f=d*const):
    nominator = 2 * A * d * s_0 * (s_0 - f) * f ** (2)
    denominator = f ** (4) - A ** (2) * d ** (2) * s_0 ** (2)
    return nominator / denominator


def var(v):
    return np.linspace(v-v/8, v+v/2, 100)


x = var(d)

fig, ax = plt.subplots()
ax.plot(x, dof(f=x), label="A=16, d=0.004cm, s_0=275cm")
ax.set_ylabel("Field of View")
ax.set_xlabel("f / cm")
ax.legend()
plt.show()


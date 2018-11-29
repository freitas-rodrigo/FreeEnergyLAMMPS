"""
  This script collects the data from forward and backward switchings and computed the absolute free energy for each temperature.

  Usage:
    python integrate.py
"""

from numpy import *
from scipy.integrate import cumtrapz
import scipy.constants as sc

T0 = 100 # Reference temperature [K]
kB = sc.value('Boltzmann constant in eV/K') 

# Load free energy reference value.
T, F0 = loadtxt('../../frenkel_ladd/data/processed/free_energy.dat', unpack=True, usecols=[0,1])
F0 = F0[T==T0]

# Load potential energy and lambda.
U_f, lamb_f = loadtxt('../data/forward.dat', unpack=True)
U_b, lamb_b = loadtxt('../data/backward.dat', unpack=True)

# Fix adapt also scales the potential energy, so we unscale it here.
U_f /= lamb_f
U_b /= lamb_b

# Compute work done using cummulative integral.s
I_f = cumtrapz(U_f,lamb_f,initial=0)
I_b = cumtrapz(U_b[::-1],lamb_b[::-1],initial=0)
W = (I_f+I_b) / (2*lamb_f)

# Compute free energy and save results.
T = T0 / lamb_f
F = zeros(len(T))
F = F0/lamb_f + 1.5*kB*T*log(lamb_f) + W
savetxt('../data/free_energy.dat', transpose([T,F]),
        header='T [K] F [eV/atom]', fmt='%6.1f %.4f')

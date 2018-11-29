"""
  This script collects the data from forward and backward switchings and computed the absolute free energy for each temperature.

  Usage:
    python integrate.py
"""

from numpy import *
import scipy.constants as sc

# Input parameters.
T = array([   100,    400,    700,   1000,   1300,   1600]) # [A]
a = array([2.8841, 2.9115, 2.9315, 2.9484, 2.9637, 2.9782]) # [eV/A^2]
k = array([ 5.787,  4.866,  4.073,  3.373,  2.799,  2.443]) # [K]

# Constants and parameters.
m = 55.845 # Iron mass [g/mol]
natoms = 250 # Number of atoms.
kB = sc.value('Boltzmann constant in eV/K')
eV = sc.value('electron volt')
hbar = sc.value('Planck constant over 2 pi in eV s')
mu = sc.value('atomic mass constant')

################################################################################
# Lambda integration: forward and backward.
################################################################################

W = zeros(len(T)) # Reversible work for each temperature.
Q = zeros(len(T)) # Dissipation for each temperature.

for i in range(len(T)):
  # Forward integration.
  dE, lamb = loadtxt('../data/thermo/forward_%dK.dat' % T[i], unpack=True)
  I_forw = trapz(dE,lamb)
  
  # Backward integration.
  dE, lamb = loadtxt('../data//thermo/backward_%dK.dat' % T[i], unpack=True)
  I_back = trapz(dE,lamb)

  # Compute reversible work and dissipation.
  W[i] =  (I_forw-I_back) / 2
  Q[i] = -(I_forw+I_back) / 2

################################################################################
# Compute free energy.
################################################################################

# Setup reference system free energy.
omega  = sqrt(k*eV/(m*mu)) * 1.0e+10 # [1/s]
F_harm = 3*natoms*kB*T * log(hbar*omega/(kB*T))

# Fixed center of mass correction.
V = (a**3/2.0) * natoms # Total volume.
F_CM = (kB*T)*log((natoms/V) * (2*pi*kB*T / (natoms*k))**(3./2.))

# Compute absolute free energy and normalize
F = (F_harm + W + F_CM) / natoms
Q /= natoms

# File output.
savetxt('../data/processed/free_energy.dat', transpose([T, F, Q]),
        header='T [K] F [eV/atom] Q [eV/atom]', fmt='%4d %.4f %.4f')

################################################################################

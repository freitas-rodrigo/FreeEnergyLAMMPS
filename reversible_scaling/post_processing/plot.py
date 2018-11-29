"""
  This script plots the free energy vs temperature, as computed using the Frenkel-Ladd and the Reversible Scaling methods.

  Usage:
    python plot.py
"""

from numpy import *
import matplotlib.pyplot as plt                 
c = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', '#FFFF33', '#A65628', '#F781BF', '#999999']

################################################################################
# Load and process data.                                                       #
################################################################################

T_rs, F_rs = loadtxt('../data/free_energy.dat', unpack=True)
T_fl, F_fl = loadtxt('../../frenkel_ladd/data/processed/free_energy.dat', unpack=True, usecols=[0,1])

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(T_rs, F_rs, '-', c='k', lw=1, label='Reversible Scaling')
ax.plot(T_fl, F_fl, 'o', c=c[0], label='Frenkel-Ladd')
 
# Add details and save figure.
ax.set_xlabel(r'Temperature [K]')
ax.set_ylabel(r'Free energy [eV/atom]')
ax.legend(loc='best')
fig.savefig("fig_free_energy_vs_temperature.png", dpi=300)
plt.close()

################################################################################

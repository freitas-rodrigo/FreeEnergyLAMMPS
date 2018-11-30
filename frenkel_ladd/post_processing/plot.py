"""
  This script plots the free energy vs temperature computed from the Frenkel-Ladd thermodynamic integration.

  Usage:
    python plot.py
"""

from numpy import *
import matplotlib.pyplot as plt                 
c = ['#E41A1C','#377EB8','#4DAF4A','#984EA3','#FF7F00','#FFFF33','#A65628','#F781BF','#999999']

################################################################################
# Load data.                                                                   #
################################################################################

T, F = loadtxt('../data/processed/free_energy.dat', unpack=True)

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.80,0.80])

# Plot.
ax.plot(T, F, 'o-', c=c[0], lw=1)
 
# Add details and save figure.
ax.set_xlabel(r'Temperature [K]')
ax.set_ylabel(r'Free energy [eV/atom]')
fig.savefig("fig_free_energy_vs_temperature.png", dpi=300)
plt.close()

################################################################################

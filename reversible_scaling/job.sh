#!/bin/bash
# This script executes a single LAMMPS simulations.

lammps="../../lammps/src/lmp_serial" # Path to LAMMPS executable.

mkdir -p data # Create directory structure for data output.

# Run job.
${lammps} -in in.lmp -log data/lammps.log -screen none -var RANDOM ${RANDOM}

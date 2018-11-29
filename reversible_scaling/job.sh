#!/bin/bash
# This bash script executes sequentially a seriers of LAMMPS simulations at different temperatures.
# Usage: bash job.sh

lammps="../../lammps/src/lmp_serial" # Path to LAMMPS executable.

mkdir -p data # Create directory structure for data output.

${lammps} -in  in.lmp -log data/lammps.log -screen none -var RANDOM ${RANDOM}

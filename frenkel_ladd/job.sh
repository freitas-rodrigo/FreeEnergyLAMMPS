#!/bin/bash
# This script executes sequentially a series of LAMMPS simulations at different temperatures.

lammps="lmp_serial" # Path to LAMMPS executable.

# Setup list of parameters to loop over.
T=(   100    400    700   1000   1300   1600)
a=(2.8841 2.9115 2.9315 2.9484 2.9637 2.9782)
k=( 5.787  4.866  4.073  3.373  2.799  2.443)

mkdir -p data # Create directory structure for data output.

# Run job.
for n in $(seq 0 5)
do
  printf "Running T = ${T[n]}K simulation.\n"
  ${lammps} -in  in.lmp                   \
            -log data/lammps_${T[n]}K.log \
            -screen none                  \
            -var RANDOM ${RANDOM}         \
            -var T ${T[n]}                \
            -var a ${a[n]}                \
            -var k ${k[n]}
done

# Free-energy calculation of solids using LAMMPS
This repository hosts two examples on how to compute the free energy of solids using [LAMMPS](http://lammps.sandia.gov/). The simulations are small enough to be run in a laptop in about 2min. The methods for free-energy calculation are the Frenkel-Ladd and the Reversible Scaling. Details about algorithm implementation, syntax, and theoretical aspects can be found in

["Nonequilibrium free-energy calculation of solids using LAMMPS"  
Rodrigo Freitas, Mark Asta, and Maurice de Koning.  
Computational Materials Science  
DOI:10.1016/j.commatsci.2015.10.050](https://doi.org/10.1016/j.commatsci.2015.10.050)

## Installation
LAMMPS needs to be compiled with some nonstandard packages in order to be able to perform free energy calculations. Follow the commands below in order to install LAMMPS. Starting from an empty directory use the following commands:
```
git clone https://github.com/lammps/lammps.git lammps
cd lammps/src
cp EXTRA-FIX/fix_ti_spring.* .
make yes-MANYBODY
make -j 8 serial
```

This will create an executable named `lmp_serial` inside `lammps/src`. Go back to the original directory and clone this repository:

```
cd ../..
git clone https://github.com/freitas-rodrigo/FreeEnergyLAMMPS.git
cd FreeEnergyLAMMPS
```

Now you should be ready to run free-energy calculations of solids.

## Usage
The documentation for the commands used during free-energy calculations is available [here](https://lammps.sandia.gov/doc/fix_ti_spring.html). Alternatively, a detailed explanation of the method can be found [here](https://doi.org/10.1016/j.commatsci.2015.10.050).

Notice that in the LAMMPS input scripts, the `fix ti/spring` should be declared _before_ any other fix that modifies the forces on the particles (such as thermostats). This is necessary because one of the actions of `fix ti/spring` is to scale all forces on the particles, hence any forces added by `fix` commands declared before `fix ti/spring` will be wrongly modified.

## Examples
The two examples below demonstrate how to compute the free energy of the body-centered cubic (bcc) phase of iron at zero pressure for temperatures ranging from 100K to 1600K. The interatomic potential employed is the EAM potential described [here](https://doi.org/10.1103/PhysRevB.57.5140), available in this repository: [`Fe.eam`](Fe.eam). By following the examples below you should be able to reproduce Figure 3 of [this](https://doi.org/10.1016/j.commatsci.2015.10.050) article.

### Example 1: Frenkel-Ladd method.
The Frenkel-Ladd simulation can be run with the following commands:
```
cd frenkel_ladd
bash job.sh
```
In my personal laptop it took about 40 seconds to run the calculation for 6 different temperatures. After the calculations are done, it is necessary to perform the lambda integration and plot the results:
```
cd post_processing
python integrate.py
python plot.py
```
You will need python's modules [numpy](http://www.numpy.org/) and [matplotlib](https://matplotlib.org/) installed to run the post-processing scripts. If the code ran correctly you should obtain the following figure:
<p align="center">
  <img src="https://i.ibb.co/Vj5FtWx/fig-free-energy-vs-temperature-FL.png" width="400"/>
</p>

### Example 2: Reversible Scaling method.
Once the Frenkel-Ladd calculation is done, the Reversible Scaling simulation can be run using the following commands:
```
cd ../../reversible_scaling
bash job.sh
```
In my personal laptop it took about 15 seconds to run the simulation. After the calculation is done, it is necessary to perform the lambda integration and plot the results:
```
cd post_processing
python integrate.py
python plot.py
```
If the code ran correctly you should obtain the following figure:
<p align="center">
  <img src="https://i.ibb.co/sy9J5Zg/fig-free-energy-vs-temperature-RS.png" width="400"/>
</p>

This figure reproduces the results of Figure 3 of [this](https://doi.org/10.1016/j.commatsci.2015.10.050) article.

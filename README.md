# 23DNPs_and_me
DFT datasets for training machine learning atomistic potentials, final verision of all DNPs, LAMMPS/VASP validation calculation scripts and structure files.

We trained deep neural network potentials (DNPs) using the [deepMD-kit] ( https://github.com/deepmodeling/deepmd-kit/releases/tag/v2.1.2 ) for 23 elements accross the periodic table.

Three randomly seeded DNPs were generated for each potential.  Up to three iterations of adaptive learning refinement were applied to reduce standard deviations amoung these randomly seed DNPs. The final iterations of these DNPs can be located in the " [DNPs](https://github.com/saidigroup/23DNPs_and_me/tree/main/DNPs ) " directory

The "Training_Data" directory contained all of the training data used for fitting of the DNPs for each element.  Both the VASP trajectories and the *.npy files are located in these compressed files.

All of the structures used for validation of these DNPs can be found in the "Valdiation" directories for each element.  The relaxed.in is the LAMMPS script for generating relaxed structures and calulating the energies of these structures as well and reporting the cell dimensions.  The heat.in LAMMPS script was used to heat 10x10x10 supercell from 0 to the melting temperature for each element to demonstrat the DNP's stability for the solid phase.  The INCAR_*** is the VASP input script we used to generate the corresponding VASP reference data and compare with the LAMMPs-DNP results.   

The data used to produce figures are located in the Figures directories along with the python scripts to make these plots.  

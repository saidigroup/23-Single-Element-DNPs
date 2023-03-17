# 23DNPs_and_me
DFT datasets for training machine learning atomistic potentials, final DNP verision, and example LAMMPS/VASP validation scripts

We trained deep neural network potentials (DNPs) using the deepMD-kit ( https://github.com/deepmodeling/deepmd-kit/releases/tag/v2.1.2 ) for 23 elements accross the periodic table.
Three randomly seeded DNPs were generated for each potential.  Up to three iterations of adaptive learning refinement were applied to reduce standard deviations amoung these randomly seed DNPs.
The final iterations of these DNPs can be located in the " DNPs " folder.


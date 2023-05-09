# Description of the Training Datasets and files

INCAR.ref:
The file INCAR.ref is a general VASP INCAR file that we utilized to generate the training data from the parent POSCAR structures using NVT. 
The temperature begin and end need to be modified for the specific values desired for each element (e.g. 0.25 Tm and Tm) ****Tm is the element's metling temperature ***

input.json and out.json:
The DeepMD-kit with the compatible verison of LAMMPS code, used in this work, can be found here https://github.com/deepmodeling/deepmd-kit/releases/tag/v2.1.2.  
We utilized both the CPU and GPU verisions and reccommend using the conda based install. 

The input.json file is an example the deepMD-kit fitting parameters used for each elements final iteration.  

For each randomly seeded fitting of the training data we modified  "training": { "seed": 9999999,   with discinct values. 

Additionally the paths element specific training data ("training_data": { "systems": [ XXXXXXXX ], must be replaced. These training are found in the element specific Training_Data folder as compressed file(s).

As well as element ID "type_map" [ "Al" ] with the apropiate elemental symbol (e.g., Al, Kr, Pb, etc).

lcurve.out:
lcurve.out is the example corresponding output from the training of the Element-iteration-0.pb potential ( e.g., Co-2-0.pb ) using the DeepMD-Kit.

Compressed Training data files ( VASP files, *.raw , *.npy ):

There are two similar data directory structures we use for the training data organization one for the initial data set and one for the adaptive learning data.

Initial dataset (iteration 0 )
temperature/structure ID/sub structure/specific structures/set.000

temperature:         This is the temperature the NVT trajectories were generated at.
structure ID:        Either a Material Project ID, NOMAD database ID, or a lattice phase abbreviate ( indicates structures generated by us )
sub structure:       There are three groups elastic, interstitials, or vacancies
specific structres:  These are the specific structures whether distorted lattices (elastic), insterstials (e.g., octahedral interstitial structure) or vacancies (only single vacancy structures).
                     VASP files can be found in the specific strucutres folders as well as the *.raw data files.    
set.000:             This directory contains the *.npy files used to train the DNP models.

Adaptive Learning (iterations 1-3 )
structure ID/sub structure/specific structures/temperature/set.000

There are additional directories located in the temperature name with numbers.  These are the structures selected by the ensemble approach which are where found to be between 0.07-2 eV/nm when comparing the DNPs from a single element.
The VASP files are located in these numbered folders.  The *.raw data files are located in the temperature directory and the *.npy are located in the set.000 directory.

VASP files:           CONTCAR, POSCAR(S), OSZICAR, stdout, and vasprun.xml.  The OUTCAR files are excluded due to their large file size.  
                      The *.raw and *.npy files can be generated from the vasprun.xml (or OUTCAR) using the DeepMD-kit tools. 


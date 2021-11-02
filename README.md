# QE_scripts
Important Quantum Espresso Scripts

Average.x 
awin is the size of the window for macroscopic averages.

From the WorkFct_example in QE version 4.3.2, awin = 3.835000000 obtained by first multiplying celldm(1) and  celldm(3) and then dividing the outcome of the multiplication 
by the number layers in the bulk of the material( ie number of layers in slab+number of layers of vacuum).

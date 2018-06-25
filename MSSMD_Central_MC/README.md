# Central MC DarkSUSY 
Note: The model implementation is now in the [model database](https://feynrules.irmp.ucl.ac.be/wiki/MSSMD) in FeynRules. Make sure to cite the reference before use in public.

## Prepare cards
Central MC is different to private MC. 
All cards (MSSMD_\*) must be prepared beforehand and upload to central card repository. 

Then, we need to modify the `gridpack_generation.sh` script in order to, 
1) get the UFO model from a private repository since it's not in the central model DB yet; 
2) to accomodate our parameter change (dark photon and n1 mass, etc), copying customized `param_card.dat` to the UFO model folder for each different mass points. 

Finally, changing the lifetime of the dark photon need to be done when LHE is created from the `runcmsgrid_LO.sh` script.

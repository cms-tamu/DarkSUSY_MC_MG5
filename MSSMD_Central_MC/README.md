# Central MC DarkSUSY 
Note: The model implementation is now in the [model database](https://feynrules.irmp.ucl.ac.be/wiki/MSSMD) in FeynRules. Make sure to cite the reference before use in public.

## Prepare cards
Central MC is different to private MC. 
All cards (MSSMD_\*) are uploaded to central card repository in cms-sw/genproductions/bin/MadGraph5_aMCatNLO/cards/2017/13TeV/MSSMD. 

The `gridpack_generation.sh` script is modified in order to, 
1) get the UFO model from a private repository since it's not in the central model DB yet; 
2) to accomodate our parameter change (dark photon and n1 mass, etc), copying customized `param_card.dat` to the UFO model folder for each different mass points. 

The `runcmsgrid_LO.sh` script is modified to run the lifetime script for the dark photon once LHE is created.

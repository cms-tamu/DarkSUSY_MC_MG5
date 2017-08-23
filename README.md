# DarkSUSY MC three dimuons final state 

## Create a directory in lxplus and upload the package to the directory

`mkdir ~/MadGraph5`
 
`cd ~/MadGraph5`

## Download the MAdGraph5 package

`cp /afs/cern.ch/cms/generators/www/MG5_aMC_v2.5.5.tar.gz ./`

## Unzip the package and a folder "MG5_aMC_v2_5_5" will be created

`tar -xzf MG5_aMC_v2.5.5.tar.gz`

## Set up process pp -> Higgs through a top loop(QED=0 QCD=99)

Go to the folder "MG5_aMC_v2_5_5". Edit the file `Template/LO/Cards/proc_card_mg5.dat` to be same as:

    import model heft_v4
    # Define multiparticle labels
    define p = g u c d s u~ c~ d~ s~
    define j = g u c d s u~ c~ d~ s~
    define l+ = e+ mu+
    define l- = e- mu-
    define vl = ve vm vt
    define vl~ = ve~ vm~ vt~
    # Specify process(es) to run
    generate p p > h QED=0 QCD=99 HIG=1
    # Output processes to MadEvent directory
    output pp_to_Higgs_HEFT_Model -nojpeg

## Setup the specified process
Run `./MG5_aMC_v2_5_5/bin/mg5_aMC Template/LO/Cards/proc_card_mg5.dat` and a folder called "pp_to_Higgs_HEFT_Model" will be generated. 

Use `firefox pp_to_Higgs_HEFT_Model/index.html` to check the specified process.

Specify the model parameters `cd MG5_aMC_v2_5_5/bin/pp_to_Higgs_HEFT_Model/Cards/` and change the Higgs mass to

    25     1.25000000E+02   # H        mass

## Generate unweighted events

`cd /MadGraph5/MG5_aMC_v2_5_5/bin/PROC_heft_v4_0/bin`

`./generate_events`

The lhe.gz file along with a txt setting file will be generated under `MG5_aMC_v2_5_5/bin/pp_to_Higgs_HEFT_Model/Events` directory.

Unzip the file to get the .lhe file:

`gunzip -d *.lhe.gz`

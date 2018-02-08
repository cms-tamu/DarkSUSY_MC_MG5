# DarkSUSY MC three dimuons final state 

## Create a directory in lxplus and upload the package to the directory

`mkdir ~/MadGraph5`
 
`cd ~/MadGraph5`

## Download the MAdGraph5 package

`cp /afs/cern.ch/cms/generators/www/MG5_aMC_v2.5.5.tar.gz ./`

## Unzip the package and a folder "MG5_aMC_v2_5_5" will be created

`tar -xzf MG5_aMC_v2.5.5.tar.gz`

## Set up process pp -> Higgs through a top loop(QED=0 QCD=99)

Go to the folder "MG5_aMC_v2_5_5". Edit the file `proc_card.dat` to be same as:

    import model heft
    # Define multiparticle labels
    define p = g u c d s u~ c~ d~ s~
    define j = g u c d s u~ c~ d~ s~
    define l+ = e+ mu+
    define l- = e- mu-
    define vl = ve vm vt
    define vl~ = ve~ vm~ vt~
    # Specify process(es) to run
    generate p p > h QED=0 QCD=99 HIG=1, h > n2 n2, n2 > n1 zd, zd > mu- mu+
    # Output processes to MadEvent directory
    output pp_to_Higgs_HEFT_Model -nojpeg

## Setup the specified process
Run `./MG5_aMC_v2_5_5/bin/mg5_aMC proc_card.dat` and a folder called "pp_to_Higgs_HEFT_Model" will be generated. 

Use `firefox pp_to_Higgs_HEFT_Model/index.html` to check the specified process.

## Generate unweighted events

`cd /MadGraph5/MG5_aMC_v2_5_5/pp_to_Higgs_HEFT_Model/bin`

`./generate_events`

The lhe.gz file along with a txt setting file will be generated under `MG5_aMC_v2_5_5/pp_to_Higgs_HEFT_Model/Events` directory.

Unzip the file to get the .lhe file:

`gunzip -d *.lhe.gz`

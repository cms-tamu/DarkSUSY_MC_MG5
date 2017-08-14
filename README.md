# DarkSUSY_MC_MadGraph5_aMC-NLO

## Download the MAdGraph5 package

https://launchpad.net/mg5amcnlo

## Create a directory in lxplus and upload the package to the directory

`mkdir ~/MadGraph5`

`cd ~/MadGraph5`

`scp ~/MG5_aMC_v2.5.5.tar.gz username@lxplus.cern.ch:~/MadGraph5`

## Unzip the package and a folder "MG5_aMC_v2_5_5" will be created

`tar -xzf MG5_aMC_v2.5.5.tar.gz`

## Make a clean copy of the Template folder

`cp -r Template pp_to_Higgs_HEFT_Model`

## Set up process pp -> Higgs through a top loop(QED=0 QCD=99)

Edit the file `pp_to_Higgs_HEFT_Model/LO/Cards/proc_card_mg5.dat` to be same as:

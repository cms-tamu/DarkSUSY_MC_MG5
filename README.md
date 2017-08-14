# DarkSUSY MC three dimuons final state 

## Download the MAdGraph5 package

https://launchpad.net/mg5amcnlo

## Create a directory in lxplus and upload the package to the directory

`mkdir ~/MadGraph5`

`cd ~/MadGraph5`

`scp ~/MG5_aMC_v2.5.5.tar.gz username@lxplus.cern.ch:~/MadGraph5`

## Unzip the package and a folder "MG5_aMC_v2_5_5" will be created

`tar -xzf MG5_aMC_v2.5.5.tar.gz`


## Set up process pp -> Higgs through a top loop(QED=0 QCD=99)

Edit the file `Template/LO/Cards/proc_card_mg5.dat` to be same as:

`import model sm`
`import model heft_v4`
`# Define multiparticle labels`
`define p = g u c d s u~ c~ d~ s~`
`define j = g u c d s u~ c~ d~ s~`
`define l+ = e+ mu+`
`define l- = e- mu-`
`define vl = ve vm vt`
`define vl~ = ve~ vm~ vt~`
`# Specify process(es) to run`
`generate p p > h QED=0 QCD=99 HIG=1`
`# Output processes to MadEvent directory`
`output -f`

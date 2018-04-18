# DarkSUSY MC MG5

## Create a directory and upload the package to the directory

    mkdir ~/MadGraph5
    cd ~/MadGraph5
    cp /afs/cern.ch/cms/generators/www/MG5_aMC_v2.6.1.tar.gz ./
    tar -xzf MG5_aMC_v2.6.1.tar.gz

## Get UFO model 
Go to the folder `MG5_aMC_v2_6_1/models`. Copy the UFO model here and unzip it:

    wget https://github.com/weishi10141993/DarkSUSY_MC_MG5/blob/master/MSSMDarkSector/MSSMD_UFO.zip

## Set up processes
Edit the file `MG5_aMC_v2_6_1/proc_card.dat` to be same as:

    import model heft
    # Define multiparticle labels
    define p = g u c d s u~ c~ d~ s~
    define j = g u c d s u~ c~ d~ s~
    define l+ = e+ mu+
    define l- = e- mu-
    define vl = ve vm
    define vl~ = ve~ vm~
    import model MSSMD_UFO
    # Specify process(es) to run
    generate p p > h01,(h01 > n1 n1, (n1 > ad nD, ad > mu+ mu-))
    # Output processes to MadEvent directory
    output DarkSUSY -nojpeg

## Check the process
Run `./MG5_aMC_v2_6_1/bin/mg5_aMC proc_card.dat` and a folder called `DarkSUSY` will be generated. 

Use `firefox DarkSUSY/index.html` to check the process.

## Edit model parameters
The model parameters include masses and widths for particles and coupling constants. They are defined in file `param_card.dat` in the `DarkSUSY/Cards` folder.

## Generate events 

    cd /MadGraph5/MG5_aMC_v2_6_1/DarkSUSY/bin
    ./generate_events

The lhe.gz file along with a txt setting file will be generated under `MG5_aMC_v2_6_1/DarkSUSY/Events` directory.

Unzip the file to get the .lhe file:

    gunzip -d *.lhe.gz

Repeat generation for other masses of Higgs by editing the higgs mass in param_card.dat.

## Change dark photon lifetime

    wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMDarkSector/replace_lifetime_in_LHE.py
    python replace_lifetime_in_LHE.py > unweighted_events.lhe

## LHE Validation
    wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMDarkSector/LHE_read.py
    python LHE_read.py

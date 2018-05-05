# Private DarkSUSY MC in MG5

## Create a directory and upload the package to the directory

    mkdir ~/MadGraph5
    cd ~/MadGraph5
    cp /afs/cern.ch/cms/generators/www/MG5_aMC_v2.6.1.tar.gz ./
    tar -xzf MG5_aMC_v2.6.1.tar.gz

## Get UFO model 
Go to the folder `MG5_aMC_v2_6_1/models`. Copy the UFO model there and unzip it to folder `MSSMD_UFO`:

    wget https://github.com/weishi10141993/DarkSUSY_MC_MG5/blob/master/MSSMDarkSector/MSSMD_UFO.zip

## Set up processes
Edit the file `MG5_aMC_v2_6_1/proc_card.dat` to be same as this [proc_card.dat](https://github.com/weishi10141993/DarkSUSY_MC_MG5/blob/master/MSSMDarkSector/proc_card.dat)

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
    python replace_lifetime_in_LHE.py > DarkSUSY_mH_125_mN1_10_mND_1_mGammaD_0p25_13TeV_cT_100_events80k.lhe

## LHE Validation
    wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMDarkSector/LHE_read.py
    wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMDarkSector/tdrStyle.py
    python LHE_read.py

#!/usr/bin/expect -f

set timeout 86400
set Pass "XXXXX"
set RSAkey "XXXXX"
set N1massName [list 10]
set N1massValue [list 1.000000e+01]
################
spawn ssh -X -Y wshi@lxplus.cern.ch
expect "Password: "
send "$Pass\r"
expect "$ "
send "tmux\r"
expect "$ "

for { set m 0 } { $m < [llength $N1massName] } { incr m } {

set N1MASSNAME [lindex $N1massName $m]
set N1MASSVALUE [lindex $N1massValue $m]

if { $N1MASSNAME in [list 10] } {
set ADmassName [list 0p4 0p7]
set ADmassValue [list 4.000000e-01 7.000000e-01]
} elseif { $N1MASSNAME in [list 30] } {
set ADmassName [list 0p25]
set ADmassValue [list 2.500000e-01]
} elseif { $N1MASSNAME in [list 60] } {
set ADmassName [list 8p5]
set ADmassValue [list 8.500000e+00]
} else {
sleep 1
}

for { set k 0 } { $k < [llength $ADmassName] } { incr k } {

set ADMASSNAME [lindex $ADmassName $k]
set ADMASSVALUE [lindex $ADmassValue $k]
set cTauName [list 0 0p05 0p1 0p2 0p5 1 2 3 5 10 20 50 100]
set cTauValue [list 0 0.05 0.1 0.2 0.5 1 2 3 5 10 20 50 100]

send "cd /afs/cern.ch/work/w/wshi/public\r"
expect "$ "
send "rm -rf gridpack1\r"
expect "$ "
sleep 2
send "mkdir gridpack1\r"
expect "$ "
send "cd gridpack1\r"
expect "$ "
send "git clone git@github.com:weishi10141993/genproductions.git genproductions -b mg26x\r"
expect "Enter passphrase for key '/afs/cern.ch/user/w/wshi/.ssh/id_rsa': "
send "$RSAkey\r"
expect "$ "
send "cd genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/MSSMD\r"
expect "$ "
#paramter card
send "sed -i '47s/1.000000e+01/$N1MASSVALUE/' UFO_param_card.dat\r"
expect "$ "
send "sed -i '63s/2.500000e-01/$ADMASSVALUE/' UFO_param_card.dat\r"
expect "$ "

send "cd ../../../../..\r"
expect "$ "
send "rm gridpack_generation.sh\r"
expect "$ "
send "rm runcmsgrid_LO.sh\r"
expect "$ "
send "wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMD_Central_MC/gridpack_generation.sh\r"
expect "$ "
send "wget https://raw.githubusercontent.com/weishi10141993/DarkSUSY_MC_MG5/master/MSSMD_Central_MC/runcmsgrid_LO.sh\r"
expect "$ "
send "chmod a+x gridpack_generation.sh\r"
expect "$ "
send "chmod a+x runcmsgrid_LO.sh\r"
expect "$ "
send "./gridpack_generation.sh MSSMD cards/production/2017/13TeV/MSSMD\r"
expect "$ "
sleep 2

for { set j 0 } { $j < [llength $cTauName] } { incr j } {

set CTAUNAME [lindex $cTauName $j]
set CTAUVALUE [lindex $cTauValue $j]

#if there is lifetime 0, copy the tarball to the destination
if { $CTAUNAME in [list 0] } {
send "cp MSSMD_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz /afs/cern.ch/work/w/wshi/public/MSSMD_Mneu1_$N1MASSNAME\_MAD_$ADMASSNAME\_cT_$CTAUNAME\_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz\r"
expect "$ "
} else {
#if not, don't copy, replace lifetime
send "rm -rf lifetime\r"
expect "$ "
send "mkdir lifetime\r"
expect "$ "
send "cd lifetime\r"
expect "$ "
send "tar -xavf ../MSSMD_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz\r"
expect "$ "
send "cp ../cards/production/2017/13TeV/MSSMD/replace_lifetime_in_LHE.py .\r"
expect "$ "
send "sed -i '8s/100/$CTAUVALUE/' replace_lifetime_in_LHE.py\r"
expect "$ "
#make the tarball with the lifetime script inside
send "XZ_OPT=\"--lzma2=preset=9,dict=512MiB\" tar -cJpsf MSSMD_Mneu1_$N1MASSNAME\_MAD_$ADMASSNAME\_cT_$CTAUNAME\_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz mgbasedir process runcmsgrid.sh replace_lifetime_in_LHE.py gridpack_generation*.log InputCards\r"
expect "$ "
send "mv MSSMD_Mneu1_$N1MASSNAME\_MAD_$ADMASSNAME\_cT_$CTAUNAME\_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz /afs/cern.ch/work/w/wshi/public\r"
expect "$ "
send "cd ..\r"
expect "$ "
}

#end cTau
}
#end AD mass
}
#end N1 mass
}

send "exit\r"
expect "$ "

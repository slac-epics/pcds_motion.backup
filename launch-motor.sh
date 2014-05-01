#!/bin/bash

# Change to directory containing the script
homepath=`dirname $0`
cd $homepath

# Setup edm environment
source /reg/g/pcds/setup/epicsenv-3.14.12.sh

edm -x -eolc -m "MOTOR=$1" pcds_motionScreens/motor-control.edl &

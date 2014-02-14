#! /bin/bash

# Setup edm environment
source /reg/g/pcds/setup/epicsenv-3.14.12.sh

edm -x -eolc		\
 -m "LLL=SXR"		\
 -m "MOTOR=SXR:EXP:MMS:03"	\
 -m "IOC=SXR:R24:IOC:23:FLX"	\
 -m "V1=CXI:SC1:VGC:02,V2=CXI:SC2:VGC:02" \
 pcds_motionScreens/test-interlocks.edl	\
 pcds_motionScreens/motor-control.edl \
 &

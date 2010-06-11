TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

LIBRARY_IOC = pcds_motion

DBD += pcds_motion.dbd
#include definitions for any other support applications needed

pcds_motion_DBD += base.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
pcds_motion_SRCS += pcds_motion_registerRecordDeviceDriver.cpp
pcds_motion_SRCS_DEFAULT += pcds_motionMain.cpp

#Add a definition for each support application used by this application
#Order is important - most-dependent first to most-depended-on last
pcds_motion_LIBS += seq
pcds_motion_LIBS += pv
pcds_motion_LIBS += $(EPICS_BASE_IOC_LIBS)

pcds_motion_SNCFLAGS += +r
pcds_motion_SRCS     += motor-stop.stt
pcds_motion_DBD      += motor-stop.dbd
pcds_motion_DBD      += pcds_motion.dbd

#The following builds sncExample as a standalone application
#PROD_HOST += sncExample
#sncExample_SNCFLAGS += +m
#sncExample_SRCS += sncExample.stt
#sncExample_LIBS += seq pv
#sncExample_LIBS += $(EPICS_BASE_HOST_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

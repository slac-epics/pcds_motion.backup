#!/bin/bash
# Disable motor Record dbPut

/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1.DISA 1
/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1.DISP 1
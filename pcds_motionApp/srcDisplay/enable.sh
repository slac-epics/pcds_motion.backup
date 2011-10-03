#!/bin/bash
# Disable motor Record dbPut

/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1.DISP 0
/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1.DISA 0
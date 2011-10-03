#!/bin/bash
# Stop IMS motor immediately

/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1.STOP 1
/reg/g/pcds/package/epics/3.14/base/current/bin/linux-x86_64/caput $1:STOP 1
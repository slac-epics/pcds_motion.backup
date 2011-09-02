#!/bin/bash
# Stop IMS motor immediately

caput $1.STOP 1
caput $1:STOP 1
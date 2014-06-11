# MCode Firmware Comment Stripper
# ------------------------------------------------------------------------
# Author: Karl Gumerlock
#
# This utility is necessary to economize space when uploading firmware
# to IMS/Schneider Electric MCode-powered products. If comments are
# uploaded to the controller, they reside in flash. What's the point of
# that?
#
import time
import sys

if len(sys.argv) == 1:
    # No arguments passed
    print "MCode Firmware Comment Stripper"
    print "Usage: stripcomments.py INPUT_FILE [OUTPUT_FILE]"
    sys.exit(2)

if len(sys.argv) > 3:
    # Too many arguments
    print "ERROR: Too many arguments; check your syntax."
    sys.exit(3)

# Open input file
try:
    inFile = open(sys.argv[1], 'r')
except IOError:
    print "ERROR: Could not open input file " + sys.argv[1]
    sys.exit(4)

# If necessary, open output file
if len(sys.argv) == 3:
    try:
        outFile = open(sys.argv[2], 'w')
    except IOError:
        print "ERROR: Could not open output file " + sys.argv[2]
        sys.exit(5)


line = inFile.readline()
while line:
    # First catch all comment lines that start with '''
    if line[0] != '\'':
        # Substring any other lines that have in-line comments
        if '\'' in line:
    	    line = line[:(line.find('\'')-1)]
        # Strip away whitespace
        line = line.strip() 
        # Check if you're left with anything of consequence
        if line.__len__() != 0:
            if len(sys.argv) == 3:
                try:
                    # Output to file if argument was passed
                    outFile.write(line + '\n')
                except IOError:
                    print "ERROR: Could not write to output file " \
                          + sys.argv[2]
                    sys.exit(6)
            else:
                # Otherwise output to stdout
                print line

    line = inFile.readline()

inFile.close()

if len(sys.argv) == 3:
    outFile.close()

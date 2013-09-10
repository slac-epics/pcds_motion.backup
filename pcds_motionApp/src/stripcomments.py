inFile = open('ims_bootup_V3.mcode.klg', 'r')
outFile = open('ims_bootup_V3.mcode', 'w')

line = inFile.readline()

while line:
    if line[0] != '\'':
        if '\'' in line:
    	    line = line[:(line.find('\'')-1)]
        line = line.strip() 
	if line.__len__() != 0:
            outFile.write(line + '\n')
    line = inFile.readline()

inFile.close()
outFile.close()

import sys
import json

fi = open(sys.argv[1])		
for line in fi:
	line = json.loads(line)
	print line[0]+": "+str(line[1])

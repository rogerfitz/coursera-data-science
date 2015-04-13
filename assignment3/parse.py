import sys
import json

fi = open(sys.argv[1])		
for line in fi:
	line = json.loads(line)
	s=""
	for i in line[1]:
		s+=str(i)+", "
	s += " - "+line[0]
	
	print s

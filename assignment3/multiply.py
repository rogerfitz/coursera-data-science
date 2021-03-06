import MapReduce
import sys


"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents    
	if record[0]=='b':
		for i in range(5):		
			mr.emit_intermediate((i, record[2]), (record[1], record[3]))
	else:
		for j in range(5):
			mr.emit_intermediate((record[1], j), (record[2], record[3]))


	

def reducer(key, l):
    # key: word
    # value: list of occurrence counts
	total=0
	for i in range(len(l)):
		for j in range(i):
			if l[i][0]==l[j][0]:
				total+=(l[i][1]*l[j][1])

	mr.emit((key[0],key[1],total))
	
		
		
    
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

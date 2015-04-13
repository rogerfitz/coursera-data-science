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
    
    mr.emit_intermediate(0, record[1][:-10])

def reducer(key, l):
    # key: word
    # value: list of occurrence counts
	l=list(set(l))
	for i in range(len(l)):
		mr.emit((l[i]))
		
		
    
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

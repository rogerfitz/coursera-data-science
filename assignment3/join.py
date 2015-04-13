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
    
    mr.emit_intermediate(record[1], record)

def reducer(key, values):
    # key: word
    # value: list of occurrence counts
    total=""
    orders=[]
    items=[]
    for i in range(len(values)):
	if values[i][0]=="order":
		orders.append(values[i])
	else:
	 if values[i][0]=="line_item":
		items.append(values[i])

    for val in range(len(orders)):
	for i in range(len(items)):
		#orders[val].append(items[i])
		mr.emit(orders[val]+items[i])
		
		
    
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

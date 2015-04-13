import sys
import json
import string
import operator

def hw(tf):
	
	tweets=[]
	for line in tf:
		tweets.append(json.loads(line.encode('utf-8')))
	hashlist={}
	for i in range(len(tweets)):
		entities=tweets[i].get("entities")
		if entities==None:
			continue
		hashtags=entities["hashtags"]
		if hashtags==None:
			continue
		for i in range(len(hashtags)):
			hashtag=hashtags[i]["text"]
			hashtag=hashtag.encode('utf-8')
			if hashtag in hashlist:
				hashlist[hashtag]+=1
			else:
				hashlist[hashtag]=1

	sort=sorted(hashlist.iteritems(), key=operator.itemgetter(1))
	counter=1
	for i in reversed(range(len(sort))):
		if(counter>10):
			break
		counter+=1
		k,v=str(sort[i]).split("', ")
		d,k=str(k).split("'")
		v,d=str(v).split(")")
		print k+" "+v
						
	
				
	
			
			
			
def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()

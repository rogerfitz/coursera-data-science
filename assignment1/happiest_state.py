import sys
import json
import string

def hw(sf, tf):
	scores={}
	for line in sf:
		term, score=line.split("\t")
		scores[term]=int(score)
	
	tweets=[]
	for line in tf:
		tweets.append(json.loads(line.encode('utf-8')))
	tweet_score=[]
	for i in range(len(tweets)):
		if ('text' in tweets[i]):
			text=tweets[i]['text']		
			sum_sent=0
			for word in text.split():
				sum_sent+=scores.get(word, 0.0)
			tweet_score.append(float(sum_sent))
	states={}
	happiest=""
	for i in range(len(tweet_score)):
		if(tweet_score[i]!=0):
			try:
				if(tweets[i]["place"]["country_code"].lower()=="us"):
					state=tweets[i]["place"]["full_name"].split(", ")[1]
					happiest=state
					if(states[state]!=None):
						states[state].append(states[state]+tweet_score[i])
					else:
						states[state].append(tweet_score[i])
			except Exception, e:
				continue	
					
	for state in states:
		if(states[state]>states[happiest]):
			happiest=state
	print str(happiest)
	
			
			
			
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()

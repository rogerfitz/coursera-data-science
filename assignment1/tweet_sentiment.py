import sys
import re
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
			text=text.translate(string.punctuation)
			text=text.translate(string.uppercase)
			for word in text.split():
				sum_sent+=scores.get(word, 0.0)
			
			print float(sum_sent)
			
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()

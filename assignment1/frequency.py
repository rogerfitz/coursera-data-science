import json
import sys

def main():
	tf = open(sys.argv[1])

	tweets=[]
	for line in tf:
		tweets.append(json.loads(line.encode('utf-8')))
	freq={}
	total=0
	for i in range(len(tweets)):
		if ('text' in tweets[i]):
			text=tweets[i]['text']		
			for word in text.split():
				if(word in freq):
					freq[word]=1+freq[word]
				else:
					freq[word]=1
				total+=1

	for word in freq:
		print word+' '+str(float(freq[word])/float(total))


if __name__ == '__main__':
    main()

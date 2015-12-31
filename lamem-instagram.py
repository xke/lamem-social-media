import urllib2 # synchronous http loading
import json
import datetime

# this url returns a JSON of the most recent 20 images/videos. results variable should parse the "items" key
instagramURL = "https://www.instagram.com/taylorswift/media/" 


# below are alternate URL forms that get previous images. results variable should parse the "data" key

#instagramURL = "https://api.instagram.com/v1/users/11830955/media/recent?access_token=2912979.87fdd31.0949d22f4a714349ae84643c5af165ef&max_id=1088060304040849874_11830955" 
#instagramURL = "https://api.instagram.com/v1/users/11830955/media/recent?access_token=2912979.87fdd31.0949d22f4a714349ae84643c5af165ef&max_id=1078363953501761596_11830955"
#instagramURL = "https://api.instagram.com/v1/users/11830955/media/recent?access_token=2912979.87fdd31.0949d22f4a714349ae84643c5af165ef&max_id=1060697492037759175_11830955"
#instagramURL = "https://api.instagram.com/v1/users/11830955/media/recent?access_token=2912979.87fdd31.0949d22f4a714349ae84643c5af165ef&max_id=1050221392618779437_11830955"

instagramURL = "https://api.instagram.com/v1/users/11830955/media/recent?access_token=2912979.87fdd31.0949d22f4a714349ae84643c5af165ef&max_id=1041378278638547805_11830955"

memScoreBaseURL = "http://memorability.csail.mit.edu/cgi-bin/image.py?url="

req = urllib2.Request(instagramURL)
response = urllib2.urlopen(req)

results = json.loads(response.read())["data"] 

for i in range(0, len(results)):

	# skip videos
	isVideo = results[i].get("videos", False)
	if isVideo == False:
		continue # skip!

	# get photo stuff
	imageURL = results[i]["images"]["standard_resolution"]["url"]
	likes = results[i]["likes"]["count"]

	memScoreURL = memScoreBaseURL + imageURL

	createdTime = results[i]["created_time"]
	printedTime = datetime.datetime.fromtimestamp(int(createdTime)).strftime('%Y-%m-%d %H:%M:%S')

	# fetch memscore
	req = urllib2.Request(memScoreURL)
	response = urllib2.urlopen(req)
	memScoreResults = json.loads(response.read())

	print printedTime + ", " + imageURL + ", " + str(likes) + ", " + str(memScoreResults["memscore"])



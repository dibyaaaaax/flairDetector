import pymongo
import test
import preprocessing
import pickle
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb1 = myclient["mydatabase2"]
# database = mydb1["training data"]

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-lg7v7.mongodb.net/test?retryWrites=true&w=majority")
data = client.get_database('reddit')
database1 = data.posts



def extractData():
	flairs = ["Photography", "Non-Political", "AskIndia", "Sports", 
			"Business/Finance", "Casual AMA","Politics", 
			"[R]eddiquette", "Science/Technology", "Policy/Economy", "Food"]
	extractedData = []
	for flair in flairs:
		print(flair)
		post = test.findDataOn('flair:"' + flair+'"', flair)
		extractedData = extractedData + post
	return extractedData	


def createDatabase():
	#database.delete_many({})
	
	database1.delete_many({})	
	for i in extractData():
		database1.insert_one(i)



def allDataaa():

	allData =[[], [], [], [], [], [], [], [], [], []]
	features =["flair", "title", "time", "link","id", "comments", "body", "titleComments", "upvotes", "commentNum"]
	allDataaa={}
	for i in database1.find():
		allData[0].append(i["flair"])
		allData[1].append(i["title"])
		allData[2].append(i["time"])
		allData[3].append(i["link"])
		allData[4].append(i["_id"])
		allData[5].append(i["comments"])
		allData[6].append(i["body"])
		allData[7].append(i["titleComments"])
		allData[8].append(i["upvotes"])
		allData[9].append(i["commentNum"])
	for j in range(len(features)):
		entry={features[j]: allData[j]}
		allDataaa.update(entry)

	# with open ('data.pickle', 'wb') as fileHandle:
	# 	pickle.dump(allDataaa, fileHandle)

	return allDataaa


def allData():
	# with open('data.pickle', 'rb') as fileHandle:
	# 	data = pickle.load(fileHandle)
	# return data
	return allDataaa()





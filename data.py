import mongo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

flairValues={"Photography": 0, "Non-Political": 1, "AskIndia":2, "Sports":3, 
			"Business/Finance":4, "Casual AMA":5,"Politics":6, 
			"[R]eddiquette":7, "Science/Technology":8, "Policy/Economy":9, "Food":10}	

def changeListToStr(li):
	s=""
	for i in li:
		s=s+i+" "
	return s.rstrip()

allData = mongo.allData()
allData = pd.DataFrame(allData)
allData["flairNum"] = allData.flair.map(flairValues)

def splitTestTrain(x_parameter, predictMe={}):

	y = allData.flairNum
	X = allData[x_parameter]

	x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=1)

	vect = CountVectorizer()
	x_train_dtm = vect.fit_transform(x_train)
	x_test_dtm = vect.transform(x_test)

	if predictMe!={}:
		predictMe_dtm = vect.transform(predictMe)
		return x_train_dtm, x_test_dtm, y_train, y_test, predictMe_dtm

	return x_train_dtm, x_test_dtm, y_train, y_test, {}

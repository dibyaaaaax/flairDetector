from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import data
import praw
import datetime
import test
import data
import pandas as pd
import preprocessing
import naiveBayes



def getPost(url):
	post = test.reddit.submission(url= url)

	entry={}
	entry["title"] = [post.title]
	entry["comments"] = [""]

	post.comments.replace_more(limit=10)
	for comment in post.comments.list():
	    if comment.body!="[removed]":
	        entry["comments"][0]=entry["comments"][0] + " " + str(comment.body)
	entry["tb"]= [entry["title"][0]+" "+entry["comments"][0]]
	return entry


def predict(url):
	
	entry = getPost(url)
	logRe = LogisticRegression()
	preditMe = entry["tb"]

	predictedFlair = naiveBayes.prediction("titleComments", logRe, preditMe)

	return (list(data.flairValues.keys())[list(data.flairValues.values()).index(predictedFlair)])
	
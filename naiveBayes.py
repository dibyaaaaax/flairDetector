from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import data
from sklearn import metrics
from warnings import simplefilter
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

simplefilter(action='ignore', category=FutureWarning)


nb = MultinomialNB()
logRe = LogisticRegression()
rfc = RandomForestClassifier()
mlp = MLPClassifier()

def prediction(parameter, model, predictMe={}):

	x_train_dtm, x_test_dtm, y_train, y_test, predictMe = data.splitTestTrain(parameter, predictMe)
	model.fit(x_train_dtm, y_train)
	if predictMe=={}:
		predictFlair = model.predict(x_test_dtm)
		print(metrics.accuracy_score(y_test, predictFlair))
	else:
		predictFlair = model.predict(predictMe)
		return predictFlair

def modelsAccuracy():
	prediction("title", nb)
	prediction("comments", nb)
	prediction("titleComments", nb)
	print()
	prediction("title", logRe)
	prediction("comments", logRe)
	prediction("titleComments", logRe)
	print()
	prediction("title", rfc)
	prediction("comments", rfc)
	prediction("body", rfc)
	prediction("titleComments", rfc)

if __name__ == "__main__":
	modelsAccuracy()
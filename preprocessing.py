import unicodedata
import re
import inflect


def removeNonASCII(data):
	new_words=[]
	for word in data:
		new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
		new_words.append(new_word)
	return new_words

def lowerCase(data):
	for i in range(len(data)):
		temp = data[i].lower()
		data[i] = temp
	return data

def removePunctuation(data):
	new_data = []
	for word in data:
		temp = re.sub(r'[^\w\s]', '', word)
		if temp != "":
			new_data.append(temp)
	return new_data

def removeStopWords(data):
	new_data = []
	for word in data:
		if word not in nltk.corpus.stopwords.words('english'):
			new_data.append(word)
	return new_data

def numberToWords(data):
	for i in range(len(data)):
		if data[i].isdigit() and int(data[i])<3000:
			temp = inflect.engine().number_to_words(data[i])
			data[i] = temp
	return data

def stemming(data):
	for i in range(len(data)):
		temp = nltk.stem.LancasterStemmer().stem(data[i])
		data[i] = temp

	return data


def preprocess(data):
	words = nltk.word_tokenize(data)
	words = removeNonASCII(words)
	words = lowerCase(words)
	words = removePunctuation(words)
	words = removeStopWords(words)
	words = numberToWords(words)
	#words = stemming(words)
	return words


###https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
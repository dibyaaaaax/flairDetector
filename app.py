from flask import Flask, render_template, request
import predictor

app = Flask(__name__)
app.secret_key = "sdf"

@app.route('/', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':
		url=request.form['url']
		predict=predictor.predict(url)
		return render_template('index.html', predict=predict)

	return render_template('form.html')

if __name__ == '__main__':
	app.run()
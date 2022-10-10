from flask import *
app = Flask(__name__)

@app.route('/')
def message():
	return render _template('message.html',n=num)
if __name__=='__main__':
	app.run(debug = True)
from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Welcome to my Page!'

if __name__ == '__main__':
	app.run(debug = True)

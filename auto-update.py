from flask import Flask
import subprocess
import requests

app = Flask(__name__)

@app.route('/payload', methods = ['POST'])
def update():
	subprocess.Popen(['git', 'pull'])

if __name__ == '__main__':
	app.run()
	requests.post('http://104.236.191.45', data = {})


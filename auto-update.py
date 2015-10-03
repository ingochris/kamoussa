from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/payload', methods = ['GET', 'POST'])
def update():
	subprocess.Popen(['git', 'pull'])
	return 'success!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')


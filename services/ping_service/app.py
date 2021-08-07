from flask import Flask

app = Flask(__name__)

@app.route("/ping")
def hello_world():
    return "<p>Ping</p>"

if __name__ == '__main__':
	app.run(port=3001, debug=True)

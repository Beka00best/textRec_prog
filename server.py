from flask import Flask, render_template, request, redirect, url_for, render_file
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/upload", methods=["POST", GET"])


if __name__ == "__main__":
	app.run(port=5001)


from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import subprocess

MAX_FILE_SIZE = 1024 * 1024 * 10 + 1
UPLOAD_FOLDER = 'uploads'
READY_FOLDER = 'ready'
READY_FILE = 'test.txt'
PATH = "/ready/test.txt"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["POST", "GET"])
def upload():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.rsplit('.', 1)[1].lower() in ['pdf']:
            file_bytes = file.read(MAX_FILE_SIZE)
            args["file_size_error"] = len(file_bytes) == MAX_FILE_SIZE
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            args["file_fail"] = True
        args["method"] = "POST"
    return render_template("index.html", args=args)

# @app.route("/", methods=["POST", "GET"])
# def processing():
#     args = {"method": "GET"}
#     notepad = subprocess.Popen('program.py')
#     notepad.wait()
#     return render_template("index.html", args=args)

# @app.route("/", methods=["POST", "GET"])
# def send(filename):
#     args = {"method": "GET"}
#     if request.method == "POST":
#         if PATH.is_file():
#             send_from_directory(READY_FOLDER ,READY_FILE)
#         else:
#             args["no_file"] = True
#         args["method"] = "POST"
#     return render_template("index.html", args=args)

if __name__ == "__main__":
    app.run(debug=True)


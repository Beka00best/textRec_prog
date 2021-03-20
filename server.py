from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
import subprocess

MAX_FILE_SIZE = 1024 * 1024 * 10 + 1
UPLOAD_FOLDER = 'uploads'
READY_FOLDER = 'ready'
READY_FILE = 'text.txt'
PATH = "ready/text.zip"
PATH1 = "ready/textPDF.txt"
PATH2 = "ready/textOCR.txt"
PATH3 = "ready/RESULT.doc"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['READY_FOLDER'] = READY_FOLDER

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
            os.system('python3 program.py')
        else:
            args["file_fail"] = True
        args["method"] = "POST"
    return render_template("index.html", args=args)

@app.route("/<folder>/<filename>", methods=["POST", "GET"])
def download(folder, filename):
    args = {"method": "GET"}
    if request.method == "GET":
        if os.path.exists(PATH):
            return send_file(folder + '/' + filename, as_attachment=True)
        else:
            args["no_file"] = True
        args["method"] = "GET"
    return render_template("index.html", args=args)
# @app.after_request
# def remove_file(responce):
#     try:
#     except Exception as error:
#         app.logger.error("Error removing or closing downloaded file handle", error)
#     return responce

if __name__ == "__main__":
    app.run(debug=True)


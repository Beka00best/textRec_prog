from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os

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
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

@app.route("/", methods=["POST", "GET"])
def upload():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files['file']
        if file and file.filename.rsplit('.', 1)[1].lower() in ['pdf']:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_bytes = os.stat(UPLOAD_FOLDER + '/' + filename).st_size
            if file_bytes >= MAX_FILE_SIZE:
                args["file_size_error"] = True
                os.remove(UPLOAD_FOLDER + '/' + filename)
                return render_template("index.html", args=args)
            else:
                args["file_size_error"] = False
            os.system('python3 mainprog.py')
            os.remove(UPLOAD_FOLDER + '/' + filename)
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


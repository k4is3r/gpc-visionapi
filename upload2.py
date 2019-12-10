import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/upload")
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)

    file_list = request.file.getlist("file")
    for file in file_list:
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    
    return render_template("complete.html")

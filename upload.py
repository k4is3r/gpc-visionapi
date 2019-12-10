import os
from flask import Flask, render_template, request, send_from_directory
import app 
from app import analyze_photo


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

description_list = []

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
     	
    file_list = request.files.getlist("file")
    for file in file_list:
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    print(filename)
    description_list = analyze_photo(destination)
    for desc in description_list:
        print(desc.description)
     
    return render_template("complete.html", image_name=filename)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)



if __name__ == '__main__':
    app.run(debug = True)
    #port=4550

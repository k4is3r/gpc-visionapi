import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] ="./images"

 

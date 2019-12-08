import io
import os 
from google.cloud import vision
from google.cloud.vision import types

#Visio client
client = vision.ImageAnnotatorClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'car.jpg')

with io.open(file_name,'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)


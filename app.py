import io
import os 
from google.cloud import vision
from google.cloud.vision import types

def analyze_photo(filename):
    client = vision.ImageAnnotatorClient()
    descriptions=[]
    file_name = filename
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels:")
    descriptions = labels
    return descriptions 

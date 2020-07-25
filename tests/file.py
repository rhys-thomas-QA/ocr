import os, io
from google.cloud import vision
from google.cloud.vision import types
import requests
from bs4 import BeautifulSoup


image_url = ""
response = ""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision_api_token.json'

def find_image_on_webpage():
    r = requests.get("http://127.0.0.1/")
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    img = soup.img
    global image_url
    image_url = img.get('src')
    print(image_url)


def detect_document_uri():
    """Detects document features in the file located in Google Cloud
    Storage."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = image_url
    global response
    response = client.document_text_detection(image=image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def read_image():
    full_text = response.text_annotations[0].description
    lowercase=full_text.lower()
    split = lowercase.split()
    surname_index = split.index("name")
    first_name_index = split.index("birth")
    i = surname_index + 1
    array = []
    while i < first_name_index:
        array.append(split[i])
        print(split[i])
        i=i+1
    print(array)
    x = " ".join(array)
    print(x)
    # print(lowercase)
    f = open("log.txt", "w")
    f.write(full_text)
    f.close()

    length_of_doc = len(response.text_annotations)
    i=1
    while i <= length_of_doc:
        # print(response.text_annotations[i].description)
        i=i+1
    # print(response.responses[0].textAnnotations.description)

find_image_on_webpage()
detect_document_uri()
read_image()



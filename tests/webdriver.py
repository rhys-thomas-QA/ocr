from selenium.webdriver import Chrome
from selenium import webdriver
import sys
import os
from google.cloud import vision
from google.cloud.vision import types
import requests
from bs4 import BeautifulSoup

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision_api_token.json'
path = '/Users/rhysthomas/Downloads/chromedriver'
sys.path.append(path)
driver = Chrome()
driver = webdriver.Chrome()

def script():
    def get_image():
        driver.get("file:///Users\\rhysthomas\\Documents\\Tests\\ocr\\tests\\index.html")
        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        soup = BeautifulSoup(source_code, 'html.parser')
        image_array = soup.find_all('img')
        global image_link_array
        image_link_array = []
        for x in image_array:
            image_url = x.get('src')
            image_link_array.append(image_url)


    def detect_document_uri(x):
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = image_link_array[x]
        response = client.document_text_detection(image=image)
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        global full_text
        full_text = response.text_annotations[0].description
        
    # This function converts the API response to 2 different arrays which are split by each new line or by individual word
    def read_image():
        lowercase = full_text.lower()
        global split_by_newline
        split_by_newline = lowercase.split("\n")
        global split_by_word
        split_by_word = lowercase.split()


    def data_extractor(array_type, first_word, second_word, added_index, id):
        if second_word:
            x = array_type.index(first_word)
            y = array_type.index(second_word)
            i = x + added_index
            arr = []
            while i < y:
                arr.append(array_type[i])
                i = i + 1
            z = " ".join(arr)
            field = driver.find_element_by_id(id)
            field.send_keys(z)
        else:
            x = array_type.index(first_word)
            i = x + added_index
            arr = []
            arr.append(array_type[i])
            z = " ".join(arr)
            field = driver.find_element_by_id(id)
            field.send_keys(z)


    get_image()
    detect_document_uri(0)
    read_image()
    # If the 2nd page of the form comes first on the webage, this loop redos the text conversion on the first page
    if split_by_newline[0] == "step 2a":
        detect_document_uri(1)
        read_image()

    data_extractor(split_by_newline, "family name", "first names", 1, "surname")
    data_extractor(split_by_word, "names", "occupation", 1, "fname")
    data_extractor(split_by_word, "occupation", "date", 1, "occupation")
    data_extractor(split_by_newline, "number", False, 1, "mobile")
    data_extractor(split_by_word, "address", False, -3, "other")
    data_extractor(split_by_newline, "email address", "current nz", 1, "email")
    data_extractor(split_by_newline, "zealand address",  "lived here under one month?", 2, "address")
        
            
script()
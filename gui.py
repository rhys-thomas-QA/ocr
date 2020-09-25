import PySimpleGUI as sg
import requests
from selenium.webdriver import Chrome
from selenium import webdriver
import sys
import os
from google.cloud import vision
from google.cloud.vision import types
from bs4 import BeautifulSoup

driver = Chrome()
driver = webdriver.Chrome()


sg.theme('LightBrown13')  # Add a touch of color
sg.theme_background_color("white")
sg.theme_text_element_background_color("white")


# All the stuff inside your window.
layout = [[sg.Text('Scan webpage for image and convert handwriting')],
          [sg.Button('Execute'), sg.Button('Close software')],
          ]

# Create the Window
window = sg.Window('Writing Scanner', layout)
sg.theme_list()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Execute'):
        

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
        global image_url
        image_url = soup.img.get('src')


    def detect_document_uri():
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = image_url
        response = client.document_text_detection(image=image)
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        global full_text
        full_text = response.text_annotations[0].description
        

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
    detect_document_uri()
    read_image()
    data_extractor(split_by_newline, "family name", "first names", 1, "surname")
    data_extractor(split_by_word, "names", "occupation", 1, "fname")
    data_extractor(split_by_word, "occupation", "date", 1, "occupation")
    data_extractor(split_by_newline, "number", False, 1, "mobile")
    data_extractor(split_by_word, "address", False, -3, "other")
    data_extractor(split_by_newline, "email address", "current nz", 1, "email")
    data_extractor(split_by_newline, "zealand address",  "lived here under one month?", 2, "address")


script()
    if event in (None, 'Close software'):  # if user closes window or clicks cancel
        break

window.close()

import PySimpleGUI as sg
import requests
import json
import urllib.parse
import time
import sys
import os
import io
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from google.cloud import vision
from google.cloud.vision import types

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
        image_url = ""
        response = ""
        full_surname = ""
        split_by_newline = ""
        split_by_word = ""
        full_address = ""

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision_api_token.json'

        path = '/Users/rhysthomas/Downloads/chromedriver'
        sys.path.append(path)

        def login():     
            elem = driver.find_element_by_xpath("//*")
            source_code = elem.get_attribute("outerHTML")
            soup = BeautifulSoup(source_code, 'html.parser')
            img = soup.find(id="1")
            global image_url
            image_url = img.get('src')

        def detect_document_uri():
            # Detects document features in the file located in Cloud Storage.
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
            # Use the print below to debug the response from Google Vision 
            # full_text = response.text_annotations[0].description
            # print(full_text)
        

        def read_image():
            full_text = response.text_annotations[0].description
            lowercase = full_text.lower()
            global split_by_newline
            split_by_newline = lowercase.split("\n")
            global split_by_word
            split_by_word = lowercase.split()

        def surname_extraction():
            # Surname extraction
            surname_index = split_by_newline.index("family name")
            first_name_index = split_by_newline.index("first names")
            i = surname_index + 1
            array = []
            while i < first_name_index:
                array.append(split_by_newline[i])
                i = i+1
            global full_surname
            full_surname = " ".join(array).title()
            print(full_surname)


        def first_names_extraction():
            # First names extractions
            first_names_index = split_by_word.index("names")
            dob_index = split_by_word.index("occupation")
            i = first_names_index + 1
            array = []
            while i < dob_index:
                replaced = split_by_word[i].replace(".", "")
                array.append(replaced)
                i = i+1
            no_integers = [x for x in array if not (
                x.isdigit() or x[0] == '-' and x[1:].isdigit())]
            print(no_integers)
            global full_first_names
            full_first_names = " ".join(no_integers).title()
            print(full_first_names)


        def dob_extraction():
            # DOB extraction
            dob_index = split_by_newline.index("date of birth")
            occupation_index = split_by_newline.index("mobile phone")
            i = dob_index + 1
            array = []
            while i < occupation_index:
                array.append(split_by_newline[i])
                i = i+1
            global full_dob
            full_dob = " ".join(array)
            print(full_dob)


        def occupation_extraction():
            # Occupation extraction
            occupation_index = split_by_word.index("occupation")
            mobile_index = split_by_word.index("date")
            i = occupation_index + 1
            array = []
            while i < mobile_index:
                array.append(split_by_word[i])
                i = i+1
            global full_occupation
            full_occupation = " ".join(array).title()
            print(full_occupation)


        def mobile_extraction():
            # Mobile extraction
            mobile_index = split_by_newline.index("number")
            global full_mobile
            full_mobile = split_by_newline[mobile_index + 1]
            print(full_mobile)


        def other_phone_extraction():
            # Other phone number extraction
            other_phone_index = split_by_word.index("number")
            global full_other_phone
            full_other_phone = split_by_word[other_phone_index + 4]
            print(full_other_phone)


        def email_extraction():
            # Email extraction
            email_index = split_by_newline.index("email address")
            address_index = split_by_newline.index("current nz")
            i = email_index + 1
            array = []
            while i < address_index:
                array.append(split_by_newline[i])
                i = i+1
            global full_email
            full_email = "".join(array)
            print(full_email)


        def address_extraction():
            # Address extraction
            address_index = split_by_word.index("home")
            end_of_address_index = split_by_word.index("lived")
            i = address_index + 2
            array = []
            while i < end_of_address_index:
                array.append(split_by_word[i])
                i = i+1
            global full_address
            full_address = " ".join(array)
            print(full_address)

        def find_mike_elements():
            surname = driver.find_element_by_id("surname")
            surname.send_keys(full_surname)
            first_name = driver.find_element_by_id("fname")
            first_name.send_keys(full_first_names)
            # dob = driver.find_elements_by_id("dob")
            # dob.send_keys(full_dob)
            occupation = driver.find_element_by_id("occupation")
            occupation.send_keys(full_occupation)
            mobile_number = driver.find_element_by_id("mobile")
            mobile_number.send_keys(full_mobile)
            other_number = driver.find_element_by_id("other")
            other_number.send_keys(full_other_phone)
            email = driver.find_element_by_id("email")
            email.send_keys(full_email)
            address = driver.find_element_by_id("address")
            address.send_keys(full_address)

        def full_process():
            login()
            detect_document_uri()
            read_image()
            surname_extraction()
            first_names_extraction()
            occupation_extraction()
            mobile_extraction()
            other_phone_extraction()
            email_extraction()
            address_extraction()
            find_mike_elements()

        full_process()
    if event in (None, 'Close software'):  # if user closes window or clicks cancel
        break

window.close()

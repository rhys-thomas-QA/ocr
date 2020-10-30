from google.cloud import vision
from google.cloud.vision import types
import requests
import os
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision_api_token.json'


def lambda_handler(event, context):
    # def test():
    #     thing = event["key"]
    #     print("KAJSHDKJAHSD")
    #     return {
    #         'statusCode': 200,
    #         'body': thing
    #     }
    # test()
    def detect_document_uri():
        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = event['image_url']
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
    all_data_array = []

    def data_extractor(array_type, first_word, second_word, added_index):
        if second_word:
            x = array_type.index(first_word)
            y = array_type.index(second_word)
            i = x + added_index
            arr = []
            while i < y:
                arr.append(array_type[i])
                i = i + 1
            z = " ".join(arr)
            all_data_array.append(z)
        else:
            x = array_type.index(first_word)
            i = x + added_index
            arr = []
            arr.append(array_type[i])
            z = " ".join(arr)
            all_data_array.append(z)

    detect_document_uri()
    read_image()
    # TODO add in contingency for if the second form is scanned, as this will produce a 400 error
    data_extractor(split_by_newline, "family name",
                   "first names", 1)
    data_extractor(split_by_word, "names", "occupation", 1)
    data_extractor(split_by_word, "occupation", "date", 1)
    data_extractor(split_by_newline, "number", False, 1)
    data_extractor(split_by_word, "address", False, -3)
    data_extractor(split_by_newline, "email address", "current nz", 1)
    data_extractor(split_by_newline, "zealand address",
                   "lived here under one month?", 2)
    return {
        "response": all_data_array
    }

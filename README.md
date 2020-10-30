# OCR
Handwriting processor using Google Vision Optical Character Recognition

## Quickstart
Open the index.html file in a browser and click the button. This will send an API request to a Lambda that handles the Google Vision request and returns all of the needed values. 

## Setup
Run `pip3 install google.cloud.vision`, `pip3 install google.cloud`, `pip3 install pysimplegui`, `pip3 install selenium`, `pip3 install beautifulsoup4`.
Create a Google Cloud Platform account and download an API key to use the Vision OCR. Place this in the root folder. 

Chromedrive will need to be manually installed and the location of this changed in the script. Running the gui script with `python3 gui.py` will open a chrome window where you should load the HTML file `index.html` and the GUI should appear. 

Click execute to run the handwriting recognition and transfer the data to the form. 

## Setting up of Lambda and service
Copy your API key into the folder "deployment package" and zip the entire contents of the folder (do not zip the folder itself, select all inside and zip).
This is the deployment package for your AWS Lambda and can now be connected to an API via the AWS API gateway. For any further info read my blog post about this project https://rhysthomas2595.medium.com/my-journey-with-optical-character-recognition-bfe380f0d9fe


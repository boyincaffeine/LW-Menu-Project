Menu Tool by Sahil :-
This is a Python-based command-line utility that offers a wide variety of system automation features. The tool uses services from AWS, Twilio, Google, and more, integrating them into a single menu-driven interface for productivity and automation tasks.

Features :-
The script offers the following capabilities:

Text-to-Speech: Type and hear the spoken output using pyttsx3.

Google Search: Get the top 5 Google search results using googlesearch.

WhatsApp Message: Send WhatsApp messages via Twilio.

SMS: Send text messages using Twilio.

Voice Call: Make automated calls using Twilio.

Instagram Post: Upload a photo to Instagram using instagrapi.

Webcam Snapshot: Capture a photo using your webcam.

Create Image: Generate a custom image with shapes using OpenCV.

Send Email: Send emails via SMTP.

Schedule Email: Delay and send emails at a specific time.

Filtered Webcam Photo: Capture and apply edge detection to a photo.

System RAM Info: Show memory usage using psutil.

Launch EC2 Instance: Deploy a new EC2 instance via AWS Boto3.

Access CloudWatch Logs: Fetch logs from AWS CloudWatch.

AWS Transcribe: Convert an MP3 file from S3 to text.

MongoDB + Lambda: Insert data into MongoDB via AWS Lambda.

Upload File to S3: Upload a file to an AWS S3 bucket.

Bulk Email via SES: Send emails to multiple recipients listed in an S3 file.

Requirements :-
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt

Likely Dependencies:-
pyttsx3

googlesearch-python

twilio

opencv-python

numpy

boto3

instagrapi

pymongo

requests

You may need additional packages depending on your OS or Python version.

Setup :-
Configure AWS Credentials (access key and secret key hardcoded — change this to use ~/.aws/credentials or env vars for production).

Configure Twilio SID and Auth Tokens.

Ensure verified sender email for SES and recipient emails.

Set Instagram credentials in the script.

Ensure MP3 file exists in S3 for Transcribe.


Usage
Run the script:

bash
Copy
Edit
python Menu.py
Select the operation by entering the number corresponding to your choice.

Author :-
Sahil — Project developed for personal productivity and learning.

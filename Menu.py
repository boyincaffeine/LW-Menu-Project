import pyttsx3
from googlesearch import search
from twilio.rest import Client
import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from datetime import datetime
from instagrapi import Client as InstaClient
import psutil
import boto3
import paramiko
import os
import json
import time
from urllib.parse import urlparse
from pymongo import MongoClient
from bson.objectid import ObjectId
import requests
import boto3

print()
print("\t\t\t\t---------------------------------------------------------------------------")
print("\t\t\t\t-----------------     Welcome to Menu Tool by Sahil    --------------------")
print("\t\t\t\t---------------------------------------------------------------------------")
print()

def speaker():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    text = input("Enter the sentence you want to spell by your system: ")
    engine.say(text)
    engine.runAndWait()

def search_query():
    query = input("Enter the word: ")

    # Search for top 5 results
    results = search(query, num=5, stop=5)

    # Print the URLs
    for result in results:
        print(result)

def whatsapp():
    account_sid = 'Your_sid'
    auth_token = 'your token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your appointment is coming up on July 21 at 3PM',
        to='whatsapp:+919518157511'
    )
    print(message.sid)
    print("Message sent successfully!")

def message():
    account_sid = 'AC219d81a9b90'
    auth_token = 'f39f2089699'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body='Hello Aditya, this is a test SMS!',
        from_='+12566023608',
        to='+918295954066'
    )

    print(message.sid)
    print("Message sent successfully!")

def call():
    account_sid = 'AC219dd27b1579b90'
    auth_token = 'ff10ce9739f2089699'
    client = Client(account_sid, auth_token)
    
    call = client.calls.create(
        twiml='<Response><Say>Hello, this is a test call from Twilio!</Say></Response>',
        from_='+12566023608',
        to='+919467545798'
    )
    
    print(call.sid)
    print("Ringing...")

def photo():
    cap = cv2.VideoCapture(0)
    status, photo = cap.read()
    cv2.imshow("Photo", photo)
    print("Your photo!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def image():
    # Create a blank image (height, width, channels)
    height = 500
    width = 500
    channels = 3  # For RGB
    image = np.zeros((height, width, channels), dtype=np.uint8)

    # Define colors
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)

    # Draw a red rectangle
    cv2.rectangle(image, (50, 50), (200, 200), red, -1)

    # Draw a green circle
    cv2.circle(image, (300, 300), 50, green, -1)

    # Draw a blue line
    cv2.line(image, (0, 0), (500, 500), blue, 5)

    # Put some text
    cv2.putText(image, 'Hello, Numpy!', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    # Display the image
    cv2.imshow('Custom Image', image)
    print("Here is your custom image!")
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite('custom_image.png', image)

def email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'linuxtest101@gmail.com'
    sender_password = 'LinuxTest101@1'
    recipient_email = 'adityachawla0034@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

def schedule_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'linuxtest101@gmail.com'
    sender_password = 'LinuxTest101@1'
    recipient_email = 'sachindayal04@gmail.com'
    subject = 'Subject of the Email'
    body = 'This is the body of the email.'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    send_time = datetime(2024, 8, 21, 18, 0, 0)
    delay = (send_time - datetime.now()).total_seconds()

    time.sleep(max(0, delay))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

def filter_image():
    def capture_photo():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return None
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            return None
        cap.release()
        return frame

    def apply_filter(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return edges

    def main():
        photo = capture_photo()
        if photo is None:
            return
        filtered_photo = apply_filter(photo)
        cv2.imshow('Original Photo', photo)
        cv2.imshow('Filtered Photo', filtered_photo)
        print("Here is your filtered image!")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    main()

def insta():
    USERNAME = 'linuxtest001'
    PASSWORD = 'linuxtest101'
    IMAGE_PATH = r'C:\Users\adico\OneDrive\Desktop\Products\product-jpeg-1000x1000.jpg'
    CAPTION = 'I posted this image using Python'

    cl = InstaClient()

    print("Logging in to Instagram...")
    try:
        cl.login(USERNAME, PASSWORD)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    max_retries = 5
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            print("Uploading photo to Instagram...")
            media = cl.photo_upload(IMAGE_PATH, CAPTION)
            print("Photo uploaded successfully.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Photo upload failed.")

    cl.logout()
    print("Logged out from Instagram.")

def ram_read():
    total_memory = psutil.virtual_memory().total
    available_memory = psutil.virtual_memory().available
    used_memory = psutil.virtual_memory().used
    memory_percent = psutil.virtual_memory().percent

    print(f"Total Memory: {total_memory / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {available_memory / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {used_memory / (1024 ** 3):.2f} GB")
    print(f"Memory Usage: {memory_percent}%")



AWS_REGION = 'ap-southeast-2'
EC2_KEY_PAIR = 'firstEC2'
EC2_INSTANCE_TYPE = 'c3.large'
EC2_AMI_ID = 'ami-0dcc996a24283808a'

session = boto3.Session(
    region_name=AWS_REGION,
    aws_access_key_id='AKID42RX',
    aws_secret_access_key='Z940yilb5C+Pk5'
)


ec2 = session.client('ec2')
def create_ec2_client():
    ec2 = boto3.client(
        'ec2',
        region_name='ap-southeast-2',
        aws_access_key_id='4HWD42RX',
        aws_secret_access_key='Z7yilb5C+Pk5'
    )



def launch_ec2_instance():
    response = ec2.run_instances(
        ImageId=EC2_AMI_ID,
        InstanceType=EC2_INSTANCE_TYPE,
        KeyName=EC2_KEY_PAIR,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'RHEL-GUI-Instance'
                    },
                ]
            },
        ],
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Launched EC2 instance with ID: {instance_id}")
    return instance_id

aws_access_key_id = 'AKIA4GL5DYR'
aws_secret_access_key = 'wwgmItAsvheB/j+iO/vJS'
region_name = 'ap-southeast-2'  # e.g., 'us-east-1'

log_group_name = '/aws/lambda/MongoDBLambdaFunction'
log_stream_name = '2024/08/27/[$LATEST]7c6c20154c914fc0959e7eee7c0be671'
region_name = 'ap-southeast-2'  # Update with your actual region

def fetch_logs(log_group_name, log_stream_name, region_name):
    try:
        client = boto3.client('logs',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)

        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            limit=10  # Adjust as needed
        )

        logs = []
        for event in response['events']:
            logs.append({
                'timestamp': event['timestamp'],
                'message': event['message']
            })

        return logs

    except Exception as e:
        return {'error': str(e)}

def access_cloud_logs():
    logs = fetch_logs(log_group_name, log_stream_name, region_name)
    print(json.dumps(logs, indent=4))




def save_instance_id(instance_id):
    with open('instance_id.txt', 'w') as f:
        f.write(instance_id)

def load_instance_id():
    if os.path.exists('instance_id.txt'):
        with open('instance_id.txt', 'r') as f:
            return f.read().strip()
    return None


def s3_to_transcribe():
    bucket_name = "linuxbucket001"
    object_key = "transcribing_1.mp3"
    
    transcribe = boto3.client('transcribe')
    job_name = f"transcribe-{int(time.time())}"
    
    try:
        # Start transcription job
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': f's3://linuxbucket001/transcribing_1.mp3'},
            MediaFormat='mp3',
            LanguageCode='en-US'
        )
        print(f"Started transcription job: {job_name}")

        # Poll the transcription job status
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            job_status = status['TranscriptionJob']['TranscriptionJobStatus']
            if job_status in ['COMPLETED', 'FAILED']:
                break
            print(f"Job {job_name} status: {job_status}")
            time.sleep(5)

        if job_status == 'COMPLETED':
            transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
            print(f"Transcription completed. Transcript URL: {transcript_uri}")

            parsed_url = urlparse(transcript_uri)
            transcript_bucket = parsed_url.netloc  # Extract the bucket name from the URI
            transcript_key = parsed_url.path.lstrip('/')  # Extract the key from the URI

            print(f"Transcript bucket: {transcript_bucket}")
            print(f"Transcript key: {transcript_key}")

            # Check length of key
            if len(transcript_key) > 1024:
                raise ValueError(f"Transcript key is too long: {len(transcript_key)} characters")

            # Fetch the transcript directly from the transcript URI
            s3_client = boto3.client('s3')
            transcript_bucket = "aws-transcribe-ap-southeast-2-prod"
            transcript_key = '/'.join(transcript_uri.split('/')[3:])  # Extract the key from the URI

            transcript_response = s3_client.get_object(Bucket=transcript_bucket, Key=transcript_key)
            transcript_data = json.loads(transcript_response['Body'].read().decode('utf-8'))

            # Print out the transcript text
            print("Transcript:")
            print(transcript_data['results']['transcripts'][0]['transcript'])
        else:
            print(f"Transcription job {job_name} failed.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def insert_data():
    name = input("Enter the name: ")
    type_ = input("Enter the type: ")
    
    data = {
        "name": name,
        "type": type_
    }
    
    return data

def invoke_lambda(data):
    client = boto3.client('lambda')
    
    # Replace with your Lambda function name
    response = client.invoke(
        FunctionName="MongoDBLambdaFunction",
        InvocationType='RequestResponse',
        Payload=json.dumps({"data": data})
    )
    
    response_payload = json.loads(response['Payload'].read())
    print(f"Response: {response_payload}")

def upload_to_s3(bucket_name, file_path):
    s3_client = boto3.client('s3')
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file_data:
            # Upload the file to S3
            s3_client.upload_fileobj(file_data, bucket_name, os.path.basename(file_path))
        print(f"File {file_path} uploaded successfully to bucket {bucket_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Define your bucket name and file path
bucket_name = 'unique003'
file_path = r"C:\Users\adico\OneDrive\Desktop\emails.txt"

# Call the function to upload the file
upload_to_s3(bucket_name, file_path)

bucket_name = 'unique003'
object_key = 'emails.txt'  # The key you provided
def send_emails_from_s3(bucket_name, object_key):
    s3_client = boto3.client('s3')
    ses_client = boto3.client('ses')
    
    try:
        # Retrieve the object from S3
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        email_data = s3_object['Body'].read().decode('utf-8')
        
        # Extract email IDs (assuming each email ID is on a new line)
        email_ids = email_data.splitlines()
        
        # Send emails using SES
        source_email = 'linuxtest101@gmail.com'  # Replace with your verified email address
        for email_id in email_ids:
            try:
                response = ses_client.send_email(
                    Source=source_email,
                    Destination={'ToAddresses': [email_id]},
                    Message={
                        'Subject': {'Data': 'Hello from AWS Lambda!'},
                        'Body': {'Text': {'Data': 'This is a test email sent via AWS Lambda and SES.'}}
                    }
                )
                print(f"Email sent to {email_id}. Message ID: {response['MessageId']}")
            except Exception as e:
                print(f"Error sending email to {email_id}: {e}")
    except Exception as e:
        print(f"Error retrieving or processing S3 object: {e}")


print("Press 1: to Print any text and have it spoken aloud.")
print("Press 2: to Search for the top 5 results on Google.")
print("Press 3: to Send a WhatsApp message.")
print("Press 4: to Send a text message.")
print("Press 5: to Make a phone call.")
print("Press 6: to Post on Instagram.")
print("Press 7: to Click a photo using your webcam.")
print("Press 8: to Create and display an image with shapes.")
print("Press 9: to Send an email.")
print("Press 10: to Schedule an email to be sent at a specific time.")
print("Press 11: to Click a photo and apply a filter.")
print("Press 12: to Check your system's memory usage.")
print("Press 13: to Launch EC2 Instance.")
print("Press 14: to Access Logs from Cloud.")
print("Press 15: to convert the Audio file into text using aws transcribe service.")
print("Press 16: Connect to MongoDB and insert data using Lambda Function.")
print("Press 17: Upload the file  to S3 Bucket")
print("Press 18: To send EMAIL's to the verified recepients")

choice = int(input("Enter your choice: "))

if choice == 1:
    speaker()
elif choice == 2:
    search_query()
elif choice == 3:
    whatsapp()
elif choice == 4:
    message()
elif choice == 5:
    call()
elif choice == 6:
    insta()
elif choice == 7:
    photo()
elif choice == 8:
    image()
elif choice == 9:
    email()
elif choice == 10:
    schedule_email()
elif choice == 11:
    filter_image()
elif choice == 12:
    ram_read()
elif choice == 13:
    instance_id = launch_ec2_instance()
    save_instance_id(instance_id)
elif choice == 14:
    access_cloud_logs()
elif choice == 15:
    s3_to_transcribe()
elif choice==16:
    data = insert_data()
    invoke_lambda(data)
elif choice==17:
    upload_to_s3(bucket_name, file_path)
elif choice==18:
    send_emails_from_s3(bucket_name, object_key)
else:
    print("Invalid choice. Please try again.")
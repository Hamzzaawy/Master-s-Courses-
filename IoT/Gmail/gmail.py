from __future__ import print_function
import pickle
import base64
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']


def send_message(service, user_id, message):
   
   message = (service.users().messages().send(userId=user_id, body=message)
              .execute())
   print ('Message Id: %s' % message['id'])
   return message


def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
#   print (message)
  return {'raw': base64.urlsafe_b64encode(message.as_string()).decode()}




def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    sneder = "kod.iot2020@gmail.com"
    reciver = "hamzzaahmed10@gmail.com"
    subject = "Hello Sina"
    message = "Say hai to our Gmail interface :D"
    msg = create_message(sneder, reciver, subject, message)
    # print(msg)
    send_message(service,'me',msg)


    


if __name__ == '__main__':
    main()
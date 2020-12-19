from __future__ import print_function
import pickle
import os.path
import httplib2
from googleapiclient import discovery
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date
from datetime import datetime
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Ne6y6YpC4ypZSpLgi0EI_QsgSIuR-p-xbojtYIP5XkQ'
SAMPLE_RANGE_NAME = "B3:B13"
KEY = 'AIzaSyBDq3h_jepqUIYJj799-PBoHxb_vauiNYI' 
def InitSheets():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokenSheets.pickle'):
        with open('tokenSheets.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentialsSheets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokenSheets.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    return service

def readSheet():
    service = InitSheets()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    return values

def writeSingleCellSheet():
    ID = '1hh7vcsOMZJxfCZOrOBDSHdEd_9D7uq8zAi5Vc5ayPRg'
    SAMPLE_RANGE_NAME = 'A3:B3'
    service = InitSheets()
    values = [
        [
            # Cell values ...
            15
        ],
        # Additional rows ...
    ]
    body = {
        'values': values
    }
    value_input_option = "USER_ENTERED"
    result = service.spreadsheets().values().update(
        spreadsheetId=ID, range=SAMPLE_RANGE_NAME,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

def writeRangeToSheet():
    ID = '1hh7vcsOMZJxfCZOrOBDSHdEd_9D7uq8zAi5Vc5ayPRg'
    SAMPLE_RANGE_NAME = 'A3:A5'
    service = InitSheets()
    test = [[15],[20],[25]]
    value_input_option = "USER_ENTERED"
    values = [
        [
            # Cell values ...

        ],
 
        # Additional rows
    ]
    values = test
    data = [
        {
            'range': SAMPLE_RANGE_NAME,
            'values': values
        },
        # Additional ranges to update ...
    ]
    body = {
        'valueInputOption': value_input_option,
        'data': data
    }
    
    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=ID, body=body).execute()
    print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

def AppendData():
    ID = '1hh7vcsOMZJxfCZOrOBDSHdEd_9D7uq8zAi5Vc5ayPRg'
    SAMPLE_RANGE_NAME = 'A3:B5'
    service = InitSheets()
    value_input_option = "USER_ENTERED"
    
    test = [str(date.today()),str(datetime.now().time())]
    values = [
        [
            # Cell values ...
            test[0],
            test[1]
        ],
        # Additional rows ...
    ]   
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=ID, range=SAMPLE_RANGE_NAME,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells appended.'.format(result \
                                           .get('updates') \
                                           .get('updatedCells')))



# writeSheet()



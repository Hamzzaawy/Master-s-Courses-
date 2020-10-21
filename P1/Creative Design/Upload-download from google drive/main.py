# this code is built on the liberary provided by 
from __future__ import print_function
import httplib2
import os, io, json, sys

from getfilelistpy import getfilelist

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def listFiles(size):
    results = drive_service.files().list(
        pageSize=size,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

def uploadFile(filename,filepath,mimetype):
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath,
                            mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))

def downloadFile(file_id,filepath):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def createFolder(name):
    file_metadata = {
    'name': name,
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    print ('Folder ID: %s' % file.get('id'))

def searchFile(size,query):
    results = drive_service.files().list(
    pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)",q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item)
            print('{0} ({1})'.format(item['name'], item['id']))
#uploadFile('unnamed.jpg','unnamed.jpg','image/jpeg')
# downloadFile('1hMesLGxOjQ38LOkP7BRhGNxLfVerJ3jC','F:\Master\P1\CreativeDesign\project\Mine\K\T\R\images\\1.jpg')
#createFolder('Google')
# searchFile(10,"name contains 'Getting'")

Destination = 'F:\Master\P1\CreativeDesign\project\Mine\K\T\R\images'

resource = {
    "oauth2": http,
    "id": "1HHoB9HgAPYKhcqbmxz8M06G3ZNhRppjl",
    "fields": "files(name,id)",
}
# getting an order dictionary containing the informations of the Folder Id presented in the resource dic
res = getfilelist.GetFileList(resource)

# print(json.dumps(res, indent=2))  # printing the ordered dict in a readable way

# extracting a list containg multiple ditionaries each one have an Id and Name of the files in the dictionary
FileList = res["fileList"][0]["files"]
# downloading the files to the distenation folder
for i in range (len(FileList)):
    print(FileList[i])
    fileName = FileList[i]["name"]
    fileId = FileList[i]["id"]
    downloadFile(fileId, Destination + "\\" + fileName)
    

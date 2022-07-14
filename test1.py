from flask import Flask, render_template

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

@app.route("/")
def index():
  return render_template('index.html')
@app.route("/auth",methods=['POST', 'GET'])
def main():
  creds = None
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
      creds = flow.run_local_server(port=0)
      print(creds)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
      token.write(creds)
  try:
    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
      print('No labels found.')
      return
    print('Labels:')
    for label in labels:
      print(label['name'])
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f'An error occurred: {error}')

if __name__ == "__main__":
  app.run()
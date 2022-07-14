from __future__ import print_function
import os.path
import pickle
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle','rb') as token:
            creds = pickle.load(token)

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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds,token)


    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId = 'me',labelIds = ['INBOX']).execute()
    messages = results.get('messages')

    # df = pd.DataFrame(messages)
    # msg = service.users().messages().get(userId='me', id=df['id'].first(offset=1)).execute()
    # print(msg['snippet'])
    # print(type(messages))
    # print(messages)
    if not messages:
        print('no msgs')
    else:
        print('messages:')
        for message in messages:

            msg = service.users().messages().get(userId = 'me',id = message['id']).execute()
            print(msg['snippet'].first())
            print("\n")

    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    #     return
    # print('Labels:')
    # for label in labels:
    #     print(label['name'])


if __name__ == '__main__':
    main()
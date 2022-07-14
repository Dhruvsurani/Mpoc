import json
import os

import flask
import httplib2
import base64
import email
import pandas as pd
from apiclient import discovery, errors
from oauth2client import client


app = flask.Flask(__name__)


@app.route('/')
def index():
    store_dir=os.getcwd()
    if 'credentials' not in flask.session:
        return flask.redirect(flask.url_for('oauth2callback'))
    credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])
    if credentials.access_token_expired:
        return flask.redirect(flask.url_for('oauth2callback'))
    else:
        http_auth = credentials.authorize(httplib2.Http())
        gmail_service = discovery.build('gmail', 'v1', http_auth)
        results = gmail_service.users().messages().list(userId='me').execute()
        th_df = pd.DataFrame(results)
        column = list(th_df)
        print(th_df.head(1))
        msg_id = th_df['messages'][0]['id']

        # results = gmail_service.users().messages().list(userId='me').execute()  # XXXX is label id use INBOX to download from inbox
        # messages = results.get('messages', [])
        # for message in messages:
        msg = gmail_service.users().messages().get(userId='me', id=msg_id).execute()
        for part in msg['payload'].get('parts', ''):

            if part['filename']:
                if 'data' in part['body']:
                    data = part['body']['data']
                else:
                    att_id = part['body']['attachmentId']
                    att = gmail_service.users().messages().attachments().get(userId='me', messageId=msg_id,
                                                                           id=att_id).execute()
                    data = att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))

                filename = part['filename']
                print(filename)
                # path = os.path.join(store_dir + '\\' 'Downloaded files' + '\\' + filename)
                #
                # with open(path, 'wb') as f:
                #     f.write(file_data)
                #     f.close()
        # attachment_id = gmail_service.users().messages().attachments()
        # attachment_id.get()
        # print(type(attachment_id))
        # print(th_df)
        # return json.dumps(threads)
        return "Done"


@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        'credentials.json',
        scope='https://mail.google.com/',
        redirect_uri=flask.url_for('oauth2callback', _external=True)
    )
    if 'code' not in flask.request.args:
        auth_uri = flow.step1_get_authorize_url()
        return flask.redirect(auth_uri)
    else:
        auth_code = flask.request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        flask.session['credentials'] = credentials.to_json()
        return flask.redirect(flask.url_for('index'))

# @app.route('/getmail')
# def getmail():
#     if 'credentials' not in flask.session:
#         return flask.redirect(flask.url_for('oauth2callback'))
#         return flask.redirect(flask.url_for('oauth2callback'))
#     credentials = client.OAuth2Credentials.from_json(flask.session['credentials'])
#     if credentials.access_token_expired:
#         return flask.redirect(flask.url_for('oauth2callback'))
#     else:
#         http_auth = credentials.authorize(httplib2.Http())
#         gmail_service = discovery.build('gmail', 'v1', http_auth)
#         query = 'is:inbox'
#         """List all Messages of the user's mailbox matching the query.
#
#         Args:
#         service: Authorized Gmail API service instance.
#         user_id: User's email address. The special value "me"
#         can be used to indicate the authenticated user.
#         query: String used to filter messages returned.
#         Eg.- 'from:user@some_domain.com' for Messages from a particular sender.
#
#         Returns:
#         List of Messages that match the criteria of the query. Note that the
#         returned list contains Message IDs, you must use get with the
#         appropriate ID to get the details of a Message.
#         """
#         try:
#             response = gmail_service.users().messages().list(userId='me', q=query).execute()
#             messages = []
#             if 'messages' in response:
#
#                 print("************ test %s" % response)
#                 messages.extend(response['messages'])
#             while 'nextPageToken' in response:
#                 page_token = response['nextPageToken']
#                 response = gmail_service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
#                 messages.extend(response['messages'])
#
#             return messages
#         except errors.HttpError as error:
#             print('An error occurred:111111111111111111 %s' % error)


if __name__ == '__main__':
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug = True
    app.run()
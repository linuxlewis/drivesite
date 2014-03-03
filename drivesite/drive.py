import httplib2

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

from drivesite.config import config

class DriveAgent(object):

    @staticmethod
    def get_build():
        f = file(config['drive_key_path'], 'rb')
        key = f.read()
        f.close()
        credentials = SignedJwtAssertionCredentials(config['drive_email'], key,
                                                    scope='https://www.googleapis.com/auth/drive')
        http = httplib2.Http()
        http = credentials.authorize(http)
        return build('drive', 'v2', http=http)




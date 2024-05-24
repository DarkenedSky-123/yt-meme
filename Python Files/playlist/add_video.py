import os
import sys
import pickle
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Cloud Console at
# https://cloud.google.com/console.
CLIENT_SECRETS_FILE = "credentials/client.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
YOUTUBE_SCOPE = ["https://www.googleapis.com/auth/youtube"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_authenticated_service():
    creds = None
    token_path = 'credentials/seal.pickle'
    # Check if the pickle file exists
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, YOUTUBE_SCOPE)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)

def add_video_to_playlist(youtube, videoID, playlistID):
    add_video_request = youtube.playlistItems().insert(
        part="snippet",
        body={
            'snippet': {
                'playlistId': playlistID,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': videoID
                }
            }
        }
    ).execute()

if __name__ == '__main__':
    try:
        youtube = get_authenticated_service()
        add_video_to_playlist(youtube, "1zZ-8FQvp3c", "PLRRiAzvBHF8wuKEw3e5Hfq0KhzmZS_d-U")
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred: {e.content}')

import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service(name):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "Data/client.json"
    credentials_file = f"Data/{name}.pickle"

    # Load or obtain credentials
    if os.path.exists(credentials_file):
        with open(credentials_file, 'rb') as token:
            credentials = pickle.load(token)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server(port=0)
        with open(credentials_file, 'wb') as token:
            pickle.dump(credentials, token)

    # Build the service
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return youtube

def get_latest_video(channel_id):
    # Get authenticated service
    service = get_authenticated_service("seal")

    # Retrieve uploads playlist ID
    channel_request = service.channels().list(
        part='contentDetails',
        id=channel_id
    )
    channel_response = channel_request.execute()
    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve playlist items
    playlist_request = service.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=1  # Retrieve only the latest video
    )
    playlist_response = playlist_request.execute()

    # Extract latest video
    latest_video = playlist_response['items'][0]

    # Access video details
    video_id = latest_video['snippet']['resourceId']['videoId']
    # video_title = latest_video['snippet']['title']
    # video_description = latest_video['snippet']['description']
    # video_thumbnail_url = latest_video['snippet']['thumbnails']['default']['url']

    # print("Latest video:")
    # print("Title:", video_title)
    # print("Description:", video_description)
    # print("Thumbnail URL:", video_thumbnail_url)
    print("Watch it at: https://www.youtube.com/watch?v=" + video_id)
    return video_id
# Example usage:


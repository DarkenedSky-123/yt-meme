import os
import json
import requests
from googleapiclient.discovery import build
from isodate import parse_duration
import random
class YouTubeChannel:
    def __init__(self, channel_name, channel_id, api_key):
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.data_filename = "Data/thumbnails.json"
        self.previous_video_id = self.get_newest_video_id()

    def get_channel_videos(self):
        res = self.youtube.channels().list(id=self.channel_id, part='contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        videos = []
        next_page_token = None
        
        while True:
            res = self.youtube.playlistItems().list(
                playlistId=playlist_id,
                part='snippet',
                maxResults=50,
                pageToken=next_page_token
            ).execute()
            
            videos += res['items']
            next_page_token = res.get('nextPageToken')
            
            if not next_page_token:
                break

        # Sort videos by date to get the oldest one
        videos.sort(key=lambda x: x['snippet']['publishedAt'])

        return videos

    def process_channel(self):
        # Fetch the sorted list of videos
        videos = self.get_channel_videos()
        
        if videos:
            # Find the index of the previous video
            previous_video_index = next(
                (i for i, video in enumerate(videos) if video['snippet']['resourceId']['videoId'] == self.previous_video_id), -1
            )

            # Check if there is a newer video
            if previous_video_index < len(videos) - 1:
                next_video_index = previous_video_index + 1
                next_video = videos[next_video_index]

                # Get the video details
                next_video_id = next_video['snippet']['resourceId']['videoId']
                title = next_video['snippet']['title']
                duration_iso = self.youtube.videos().list(id=next_video_id, part='contentDetails').execute()['items'][0]['contentDetails']['duration']
                duration_seconds = int(parse_duration(duration_iso).total_seconds())
                video_link = f"https://www.youtube.com/watch?v={next_video_id}"
                video_thumbnail_url = f"https://i.ytimg.com/vi/{next_video_id}/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDV5LAIzvji4V898KDDLB62PUfPLA"
                # Update the previous video ID
                self.previous_video_id = next_video_id
                self.save_newest_video_id(next_video_id)

                # Return the values
                return video_thumbnail_url

        # Return None if no newer videos are found
        return None

    def get_newest_video_id(self):
        if os.path.exists(self.data_filename):
            with open(self.data_filename, 'r') as file:
                data = json.load(file)
                return data.get(self.channel_name, {}).get('video_id', None)
        return None

    def save_newest_video_id(self, video_id):
        data = {}
        if os.path.exists(self.data_filename):
            with open(self.data_filename, 'r') as file:
                data = json.load(file)

        data[self.channel_name] = {'video_id': video_id}

        with open(self.data_filename, 'w') as file:
            json.dump(data, file, indent=4)


def download_image(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the file in binary write mode and write the content
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        else:
            print("Failed to download image. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))




if __name__ == "__main__" :
        channel_names = ['memenade','memenadedm','memelion']
        channel_ids = ['UCCWp4CCmI2JmIaoAuv0ocEA','UCOsM-xMGrGH0RHffLIznrUA','UCv-6OlG8qGY-mKlE_IUkI3w']
        api_key = 'AIzaSyAAkdZaOAyVOMdSlICjgi-bfU1h1z0gmps'

        # Loop through each channel and process it
        channel_name = random.choice(channel_names)
        channel_id = channel_ids[channel_names.index(channel_name)]

        # Create an instance of the YouTubeChannel class
        youtube_channel = YouTubeChannel(channel_name, channel_id, api_key)
        # Process the channel and store the details in variables
        channel_details = youtube_channel.process_channel()

        # Store the details in variables
        download_image((channel_details),"Data/thumb.jpg")
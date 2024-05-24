# File: youtube_processor.py
from Help.vidoe_get_yt import YouTubeChannel

# Replace these with your actual channel names, IDs, and API key
channel_names = ['michaelstoren', 'chizzy', 'Ben','boeshi','Speed',"gbillz","lukelsfpxin","Buffessor","onevillage","Okcron","dzitkus"]
channel_ids = ['UCwQOKgQ-2k4Ar7QFcF0EcTg', 'UCbyCM8BZ87KEKOCz_EJP0nQ', 'UCFXCGN9-roeqdFAatAwG8ew','UCSlJ_3JEKqA7QVUJg1C7o9w','UCNFT_eq_QCApMEwCACHto9Q',"UCFTRv5q6uXHl2zwI2ANA9oA","UC7gAhc0XbQOMspFhOUY3-hw","UCjcfXqZdoCrMngD4ILYnUKQ","UCdVcQc_gdaXhlFx3UvG8pjA","UCQliobRAqnJWuFnlY9Ua0Yg","UCLmgvkCAGUhRh1Xiv3hg5HQ"]
api_key = 'AIzaSyAAkdZaOAyVOMdSlICjgi-bfU1h1z0gmps'

# Loop through each channel and process it

channel_name = channel_names[0]
channel_id = channel_ids[0]

# Create an instance of the YouTubeChannel class
youtube_channel = YouTubeChannel(channel_name, channel_id, api_key)
# Process the channel and store the details in variables
channel_details = youtube_channel.process_channel()

# Store the details in variables
processed_channel_name = channel_details['channel_name']
processed_title = channel_details['title']
processed_video_link = channel_details['video_link']
processed_duration_seconds = channel_details['duration_seconds']

# Now you can use the stored variables as needed
print(f"Processed Channel: {processed_channel_name}")
print(f"Processed Title: {processed_title}")
print(f"Processed Video Link: {processed_video_link}")
print(f"Processed Duration (seconds): {processed_duration_seconds}")

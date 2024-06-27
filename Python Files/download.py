import os
from Help.reddit import RedditMemeDownloader
from Help.youtube import YoutubeVideoDownloader
from Help.vidoe_get_yt import YouTubeChannel
from Help.download_reddit import VideoDownloader
from Help.short import VideoShortener
import requests
import random
TOKEN = os.environ['TOKEN']
CHANNEL_ID = '1240324282094190642'
SEND_message_proxy_url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "url-Type": "application/json"
}
def send_message(message):
    if not message.strip():  # Check if the message is empty or contains only whitespace
        return {"error": "Message is empty."}
    data = {
        "content": message
    }
    response = requests.post(SEND_message_proxy_url, headers=headers, json=data)
    return response.json()
def youtube_video(name):
    try:
        channel_names = ['michaelstoren', 'chizzy', 'Ben', 'boeshi', 'Speed', "gbillz", "lukelsfpxin", "Buffessor","onevillage", "Okcron", "dzitkus","Bwag","piero grieco","loic spaghetti","ItsAndrewz","Not703naz","kirkiimad","liam miller","Lord Trunks","Inhyuman","ManLikeIssac"]
        channel_ids = ['UCwQOKgQ-2k4Ar7QFcF0EcTg', 'UCbyCM8BZ87KEKOCz_EJP0nQ', 'UCFXCGN9-roeqdFAatAwG8ew','UCSlJ_3JEKqA7QVUJg1C7o9w', 'UCNFT_eq_QCApMEwCACHto9Q', "UCFTRv5q6uXHl2zwI2ANA9oA","UC7gAhc0XbQOMspFhOUY3-hw", "UCjcfXqZdoCrMngD4ILYnUKQ", "UCdVcQc_gdaXhlFx3UvG8pjA","UCQliobRAqnJWuFnlY9Ua0Yg", "UCLmgvkCAGUhRh1Xiv3hg5HQ","UCkf_EFKPgJd7Z_oJnR-Nc0Q","UCPHithq3_DTjN0QlxSrrANw","UCoEN-xBsLvDnKVxTUAzUs9A","UCk7yRx5dvXQVpLfCpG6xeZA","UCK0UNqUdxwkzKCg_ZWuiV5Q","UCiqkIF0F_6y6psq0ullRYdQ","UCWGtLkqqndu7q_SyM1X23FA","UC5ILZRGVeTwzqOhc5Ip746A","UCMBiBMt6YzPPG-sZcPG3F-g","UCj-Hs9XuzY15HE1q5R_GnJQ"]
        api_key = 'AIzaSyAAkdZaOAyVOMdSlICjgi-bfU1h1z0gmps'

        # Loop through each channel and process it
        channel_name = random.choice(channel_names)
        channel_id = channel_ids[channel_names.index(channel_name)]

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
        print(f"Processed Video Link: {processed_video_link}")
        print(f"Processed Duration (seconds): {processed_duration_seconds}")

        if 0 < int(processed_duration_seconds) <= 15:
            downloader = YoutubeVideoDownloader(processed_video_link, "Videos/"+name)
            downloader.process_video()
            short = VideoShortener("Videos/"+name)
            short.shorten_and_speedup_video()
            return True  # Return True if a video is downloaded

    except Exception as e:
        print(f"Error in youtube_video function: {e}")

    return False  # Return False if no video is downloaded

def reddit_video(name):
    try:
        names = ["funnyvideos", "MemeVideos", "TikTokCringe", "funny", "dankvideos"]
        subreddit_name = random.choice(names)
        # Create an instance of RedditMemeDownloader
        downloader = RedditMemeDownloader(subreddit_name=subreddit_name, max_merge_count=1)
        # Start downloading meme videos and get the video information list
        video_info_list = downloader.download_meme_videos()

        # Process the video information as needed
        for video_info in video_info_list:
            flair = video_info["flair"]
            video_url = video_info["video_url"]
            audio_url = video_info["audio_url"]
            video_duration = video_info["video_duration"]

            print(flair)
            print(video_url)
            print(audio_url)
            print(video_duration)

            if 0 < int(video_duration) <= 12:
                downloader = VideoDownloader(video_url, audio_url, "Videos/"+name)
                downloader.download_video()
                downloader.combine_audio_video()
                short = VideoShortener("Videos/"+name)
                short.shorten_and_speedup_video()
                return True  # Return True if a video is downloaded
            else :
                send_message("https://v.redd.it/"+video_url)


    except Exception as e:
        print(f"Error in reddit_video function: {e}")

    return False  # Return False if no video is downloaded

downloaded_count = 0
while downloaded_count < 4:
    print(f"Downloaded count: {downloaded_count}")
    functions = [reddit_video,youtube_video]
    # Randomly choose and execute a function
    random_function = random.choice(functions)
    downloaded = random_function(f"video_{downloaded_count}")

    if downloaded:
        downloaded_count += 1

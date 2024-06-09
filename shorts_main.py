import praw

username = "Armx11443"
password = "Armxisaboss123"
client_id = "PX5291z-uAykEUfeaHlGRQ"
client_secret = "oCTu3AvbxtMC7kyg9zqW6VVzsQlLHQ"

reddit_instance = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="armx"
)

print(reddit_instance.user.me())

choice = reddit_instance.subreddit("MemeVideos")
new_messages = choice.new(limit=10)

for message in new_messages:
    print("Post permalink:", message.permalink)
    print("Post URL:", message.url)
    
    if hasattr(message, 'media') and message.media is not None:
        media_info = message.media
        if 'reddit_video' in media_info:
            reddit_video = media_info['reddit_video']
            video_width = reddit_video.get('fallback_url')
            print("Video Width:", video_width)
            # Uncomment the lines below if needed for DASH quality and audio links
            # quality = f"/DASH_{video_width}.mp4"
            # print(message.url + quality)
            # print(message.url + "/DASH_AUDIO_128.mp4")
    else:
        print("No video media found.")

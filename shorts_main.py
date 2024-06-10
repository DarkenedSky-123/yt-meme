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
    print("Post permalink:", "https://reddit.com"+message.permalink)
    # print("Post URL:", message.url)
    
    if hasattr(message, 'media') and message.media is not None:
        media_info = message.media
        if 'reddit_video' in media_info:
            reddit_video = media_info['reddit_video']
            video_url = reddit_video.get('fallback_url')
            # Uncomment the lines below if needed for DASH quality and audio links
            print("Video URL:"+video_url)
            print("Audio URL:"+message.url + "/DASH_AUDIO_128.mp4")
            print("Final Link:" +f"https://sd.rapidsave.com/download.php?permalink={"https://reddit.com"+message.permalink}&video_url={video_url}&audio_url={message.url + "/DASH_AUDIO_128.mp4"}")
            print("#####################################################################################################################################")

    else:
        print("No video media found.")
    
#https://sd.rapidsave.com/download.php?permalink=https://reddit.com/r/MemeVideos/comments/1db6zwe/yeah_its_just_an_anime_its_cant_hurt_you/&video_url=https://v.redd.it/ovkaaxmhld5d1/DASH_720.mp4?source=fallback&audio_url=https://v.redd.it/ovkaaxmhld5d1/DASH_AUDIO_128.mp4

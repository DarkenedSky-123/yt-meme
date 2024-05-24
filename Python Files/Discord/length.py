from moviepy.editor import VideoFileClip

def get_video_duration(video_url):
    video = None
    try:
        # Create VideoFileClip object
        video = VideoFileClip(video_url)

        # Get the duration of the video
        duration = video.duration
        return duration
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Close the video file
        if video:
            video.close()



# Example usage
# url = "https://cdn.discordapp.com/attachments/1156671830162145430/1239765796822056960/Vegeta.mp4?ex=66441d5f&is=6642cbdf&hm=c906c8e6c10a90c85666800c186d63fdad0e8346aa791ff339d3b3ee9791dcf3&"
# duration = get_video_duration(url)

# if duration is not None:
#     print(f"Video Duration: {duration} seconds")
# else:
#     print("Failed to retrieve video duration.")
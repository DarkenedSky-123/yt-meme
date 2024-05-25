import requests
import os
import time
import json

class RedditMemeDownloader:
    def __init__(self, subreddit_name, max_merge_count=5):
        self.subreddit_name = subreddit_name
        self.max_merge_count = max_merge_count
        self.downloaded_videos = set()
        self.merge_count = 0
        self.last_downloaded_url = self.read_last_downloaded_url()

    def read_last_downloaded_url(self):
        last_downloaded_url = ""
        data_filename = "Data/subreddits_data.json"
        if os.path.exists(data_filename):
            try:
                with open(data_filename, "r") as file:
                    data = json.load(file)
                    last_downloaded_url = data.get(self.subreddit_name, {}).get('last_downloaded_url', "")
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading {data_filename}: {e}")
        return "https://v.redd.it/"+last_downloaded_url if last_downloaded_url else ""

    def download_meme_videos(self):
        video_info_list = []

        while self.merge_count < self.max_merge_count:
            try:
                endpoint = f"https://www.reddit.com/r/{self.subreddit_name}/.json?limit=200&t=all"
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(endpoint, headers=headers)
                data = response.json()

                if response.status_code == 200 and data and "data" in data and "children" in data["data"]:
                    posts = data["data"]["children"]

                    start_index = 0
                    if self.last_downloaded_url:
                        for index, post in enumerate(posts):
                            if post and "data" in post and "secure_media" in post["data"] and post["data"]["secure_media"] and "reddit_video" in post["data"]["secure_media"]:
                                video_url = post["data"]["secure_media"]["reddit_video"]["fallback_url"].split("?")[0]
                                if video_url == self.last_downloaded_url:
                                    start_index = index + 1
                                    break

                    for post in posts[start_index:]:
                        if post and "data" in post and "secure_media" in post["data"] and post["data"]["secure_media"] and "reddit_video" in post["data"]["secure_media"]:
                            video_url = post["data"]["secure_media"]["reddit_video"]["fallback_url"].split("?")[0]
                            video_url = video_url.replace("https://v.redd.it/","")
                            if "source=fallback" in video_url:
                                video_url = video_url.replace("source=fallback", "")
                                
                            audio_url_parts = video_url.split("/")
                            audio_url_parts[-1] = "DASH_AUDIO_128.mp4"
                            audio_url = "/".join(audio_url_parts)

                            flair = post["data"]["link_flair_text"] if "link_flair_text" in post["data"] else "No Flair"
                            video_duration = post["data"]["secure_media"]["reddit_video"]["duration"] if "secure_media" in post["data"] and "reddit_video" in post["data"]["secure_media"] else None

                            video_info = {
                                "flair": flair,
                                "video_url": video_url,
                                "audio_url": audio_url,
                                "video_duration": video_duration
                            }

                            video_info_list.append(video_info)
                           
                            if video_url not in self.downloaded_videos:
                                self.downloaded_videos.add(video_url)

                                self.last_downloaded_url = video_url
                                self.save_last_downloaded_url()

                                self.merge_count += 1

                                if self.merge_count >= self.max_merge_count:
                                    break

                    time.sleep(1)

                else:
                    print(f"Failed to retrieve meme videos from subreddit: {self.subreddit_name}")

            except OSError as e:
                print(f"Error: {e}. Skipping to the next URL.")
                continue

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

        return video_info_list

    def save_last_downloaded_url(self):
        data_filename = "Data/subreddits_data.json"
        data = {}
        if os.path.exists(data_filename):
            try:
                with open(data_filename, "r") as file:
                    data = json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading {data_filename}: {e}")

        data[self.subreddit_name] = {'last_downloaded_url': self.last_downloaded_url}

        os.makedirs(os.path.dirname(data_filename), exist_ok=True)
        try:
            with open(data_filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error writing to {data_filename}: {e}")

# Example usage:
# downloader = RedditMemeDownloader('funny')
# downloader.download_meme_videos()

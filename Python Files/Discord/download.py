import requests

def download_video(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Video downloaded successfully and saved to {output_path}")
    else:
        print(f"Failed to download video. HTTP Status code: {response.status_code}")

# video_url = "https://cdn.discordapp.com/attachments/1156671830162145430/1240190107479314482/Teaching_my_son_priorities.mov?ex=6645a88b&is=6644570b&hm=dad30c3f7b052044144a2b3d2615ce8f50f5b3e94884c24cf9bd1d7e55dad475&"
# output_file = "Teaching_my_son_priorities.mov"

# download_video(video_url, output_file)

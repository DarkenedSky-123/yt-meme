import subprocess
import json

# subprocess.run(["python", "Python Files/Discord/scraper.py"], check=True)

try:
        for i in range(0,1, 1):

                
                # subprocess.run(["python", "Python Files/Discord/upload.py"], check=True)
                # subprocess.run(["python", "Python Files/fps.py"], check=True)
                # subprocess.run(["python", "Python Files/Discord/join.py"], check=True)
                # subprocess.run(["python", "Python Files/delete.py"], check=True)
                subprocess.run(["python", "Python Files/Discord/upload.py"], check=True)

                print("##########################################################")
                print(f"###################### video {i+1} ###########################")
                print("##########################################################")

except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
# subprocess.run(["python", "Python Files/Discord/message.py"], check=True)
# https://www.youtube.com/shorts/4lixIz4Hw9c
# https://youtube.com/shorts/FNkEB9_wAqU?si=4SM4WV3bEWTigKqQ
import subprocess
import json
import os


try:
        for i in range(0,1, 1):
                subprocess.run(["python", "Python Files/Discord/main.py"], check=True)


                print("##########################################################")
                print(f"###################### video {i+1} ###########################")
                print("##########################################################")

except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
# subprocess.run(["python", "Python Files/message.py"], check=True)
# https://www.youtube.com/shorts/4lixIz4Hw9c
# https://youtube.com/shorts/FNkEB9_wAqU?si=4SM4WV3bEWTigKqQ

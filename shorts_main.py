import subprocess
import json
import os


try:
        for i in range(0,1, 1):
                subprocess.run(["python", "Python Files/ff.py"], check=True)
                subprocess.run(["python", "Python Files/create.py"], check=True)
                subprocess.run(["python", "Python Files/files.py"], check=True)
                subprocess.run(["python", "Python Files/daata/read_dc.py"], check=True)
                subprocess.run(["python", "Python Files/inro.py"], check=True)
                subprocess.run(["python", "Python Files/outro.py"], check=True)
                subprocess.run(["python", "Python Files/download.py"], check=True)
                subprocess.run(["python", "Python Files/fps.py"], check=True)
                subprocess.run(["python", "Python Files/join.py"], check=True)
                subprocess.run(["python", "Python Files/delete.py"], check=True)
                subprocess.run(["python", "Python Files/upload.py"], check=True)
                subprocess.run(["python", "Python Files/daata/write_dc.py"], check=True)

                print("##########################################################")
                print(f"###################### video {i+1} ###########################")
                print("##########################################################")

except json.decoder.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
# subprocess.run(["python", "Python Files/message.py"], check=True)
# https://www.youtube.com/shorts/4lixIz4Hw9c
# https://youtube.com/shorts/FNkEB9_wAqU?si=4SM4WV3bEWTigKqQ

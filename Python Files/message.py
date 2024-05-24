import requests
import time


header = {'authorization': ''}

file = "Data/Video.txt"
with open(file,"r")as f:
    ids =f.readlines(-1)
    length = len(ids)




def up(id):
    for i in range (0,length,1):
        link =("https://www.youtube.com/shorts?v="+ids[i].strip())
        payload = {'content': link}
        post =requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data = payload , headers = header)
        time.sleep(1)
    print("Done")

channels = [
    "1178974223839002666",
    "1147693763901276221",
    "1062001750317473852",
    "915657278085005343",
    "1088712797510185040",
    "882347453544816720",
    "862263994889535488",
    "1178026279631605760"
]

for i in range (0,len(channels),1):
    up(channels[i])




with open(file,"w")as f:
    f.write("")

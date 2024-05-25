import requests
import json
import os

def mess(file, id):
    TOKEN = os.environ['TOKEN']
    DATA_CHANNEL_ID = id

    # Discord API endpoint for sending messages
    SEND_MESSAGE_URL = f"https://discord.com/api/v9/channels/{DATA_CHANNEL_ID}/messages"

    # Discord API endpoint for editing messages
    EDIT_MESSAGE_URL = f"https://discord.com/api/v9/channels/{DATA_CHANNEL_ID}/messages"

    # Headers with authorization token and content type
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }

    def send_message(message):
        data = {
            "content": message
        }
        response = requests.post(SEND_MESSAGE_URL, headers=headers, json=data)
        return response.json()

    def edit_message(message_id, new_content):
        data = {
            "content": new_content
        }
        url = f"{EDIT_MESSAGE_URL}/{message_id}"
        response = requests.patch(url, headers=headers, json=data)
        return response.json()

    def read_content_from_file(filename):
        _, ext = os.path.splitext(filename)
        if ext == '.json':
            with open(filename, "r") as file:
                content = json.load(file)
            return json.dumps(content)
        elif ext == '.txt':
            with open(filename, "r") as file:
                content = file.read()
            return content
        else:
            raise ValueError("Unsupported file type")

    # Fetching the latest message ID
    response = requests.get(SEND_MESSAGE_URL, headers=headers)
    if response.status_code == 200:
        messages = response.json()
        message_content = read_content_from_file(file)
        if messages:  # If there are messages in the channel
            latest_message_id = messages[0]['id']  # Assuming the latest message is the first in the list
            # Editing the latest message with the content from the file
            response = edit_message(latest_message_id, message_content)
            print("Message edited:", response)
        else:  # If there are no messages in the channel
            # Send the message instead
            response = send_message(message_content)
            print("Message sent:", response)
    else:
        print("Failed to fetch messages.")
    
    

mess("Data/channels_data.json", "1232976045339181056")
mess("Data/subreddits_data.json", "1232976008408334356")
mess("Data/title.txt", "1243557973784268800")
mess("Data/Part.txt", "1239562583896494141")

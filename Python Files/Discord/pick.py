import json
import random

# Load JSON data from the file
def pick(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Pick a random link
    random_link = random.choice(data)

    # Print the random link
    print("Random Link:", random_link)

    # Remove the link from the list
    data.remove(random_link)

    # Update the JSON file with the modified list
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

    print("Link removed from the list.")
    return random_link

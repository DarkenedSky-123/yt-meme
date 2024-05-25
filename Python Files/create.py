import os

# Define an array of directory paths
directories = [
    "Videos",
    "Videoss",
    "Data",
    "ProcessedVideos",
    
    
]

# Create each directory
for directory in directories:
    os.makedirs(directory, exist_ok=True)

print("Directories created successfully!")

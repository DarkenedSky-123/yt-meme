import os
from moviepy.editor import VideoFileClip

def standardize_frame_rate(input_folder, output_folder, target_fps):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            video_clip = VideoFileClip(input_path)
            video_clip = video_clip.set_fps(target_fps)
            video_clip.write_videofile(output_path, codec='libx264')
            
if __name__ == "__main__":
    input_folder = "Videos"
    output_folder = "Videoss"
    target_fps = 30  # Desired frame rate
    
    standardize_frame_rate(input_folder, output_folder, target_fps)
import os
from moviepy.editor import VideoFileClip

def standardize_frame_rate(input_folder, output_folder, target_fps):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            try:
                video_clip = VideoFileClip(input_path)
                video_clip = video_clip.set_fps(target_fps)
                video_clip.write_videofile(output_path, codec='libx264')
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
                os.remove(input_path)
                print(f"Deleted {input_path} due to the error.")

if __name__ == "__main__":
    input_folder = "Videos"
    output_folder = "Videoss"
    target_fps = 30  # Desired frame rate
    
    standardize_frame_rate(input_folder, output_folder, target_fps)

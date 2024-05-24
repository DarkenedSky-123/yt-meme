import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

class VideoMerger:
    def __init__(self, input_folder, output_path, target_fps, target_resolution):
        self.input_folder = input_folder
        self.output_path = output_path
        self.target_fps = target_fps
        self.target_resolution = target_resolution

    @staticmethod
    def calculate_new_dimensions(original_size, target_resolution):
        original_width, original_height = original_size
        target_width, target_height = target_resolution

        aspect_ratio = original_width / original_height
        new_width = int(target_height * aspect_ratio)

        if new_width > target_width:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            new_height = target_height

        return new_width, new_height

    @staticmethod
    def resize_clip(clip, target_resolution):
        new_width, new_height = VideoMerger.calculate_new_dimensions(clip.size, target_resolution)
        return clip.resize((new_width, new_height))

    def merge_videos(self, intro_video_path, outro_video_path):
        video_clips = []

        # Load and resize intro video
        intro_clip = self.load_and_resize_video(intro_video_path)
        video_clips.append(intro_clip)

        # Load and resize video clips from the input folder
        self.load_and_resize_input_folder(video_clips)

        # Randomly insert outro clip between any two clips
        self.insert_outro_randomly(video_clips, outro_video_path)

        # Concatenate all clips
        self.concatenate_and_write(video_clips)

    def load_and_resize_video(self, video_path):
        video_clip = VideoFileClip(video_path)
        video_clip = video_clip.set_fps(self.target_fps)
        return video_clip.fx(self.resize_clip, self.target_resolution)

    def load_and_resize_input_folder(self, video_clips):
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".mp4"):
                video_path = os.path.join(self.input_folder, filename)
                video_clip = VideoFileClip(video_path)
                video_clip = video_clip.set_fps(self.target_fps)
                resized_clip = video_clip.fx(self.resize_clip, self.target_resolution)
                video_clips.append(resized_clip)

    def insert_outro_randomly(self, video_clips, outro_video_path):
        if len(video_clips) > 1:
            random_index = random.randint(1, len(video_clips) - 1)
            video_clips.insert(random_index, self.load_and_resize_video(outro_video_path))

    def concatenate_and_write(self, video_clips):
        if len(video_clips) > 0:
            final_clip = concatenate_videoclips(video_clips, method="compose")
            final_clip.write_videofile(self.output_path, codec='libx264', threads=4)
        else:
            print("No video files found in the input folder.")

if __name__ == "__main__":
    input_folder = "Videoss"
    output_path = "video.mp4"
    target_fps = 30  # Desired frame rate for the merged video
    target_resolution = (1280,720)  # 9:16 resolution (width, height)
    intro_video_path = "Python Files/final_output.mp4"
    outro_video_path = "Python Files/final_outro.mp4"

    video_merger = VideoMerger(input_folder, output_path, target_fps, target_resolution)
    video_merger.merge_videos(intro_video_path, outro_video_path)

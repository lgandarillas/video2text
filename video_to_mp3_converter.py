from moviepy.editor import VideoFileClip
import sys
import os
from pathlib import Path

def convert_mp4_to_mp3(video_filepath):
    """
    Converts an MP4 video file to an MP3 audio file.

    Parameters:
        video_filepath (str): The path to the MP4 video file.
    """
    video = VideoFileClip(video_filepath)
    audio = video.audio
    audio_filepath = video_filepath.replace(".mp4", ".mp3")
    audio.write_audiofile(audio_filepath)
    video.close()
    return audio_filepath

def convert_files_in_directory(directory):
    """
    Converts all MP4 files in the specified directory to MP3.

    Parameters:
        directory (str): The path to the directory containing MP4 files.
    """
    for file in Path(directory).glob("*.mp4"):
        convert_mp4_to_mp3(str(file))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python video_to_mp3_converter.py <video_file.mp4> [<video_file_2.mp4> ...] OR python video_to_mp3_converter.py <directory>")
        sys.exit(1)

    input_paths = sys.argv[1:]

    for path in input_paths:
        if os.path.isdir(path):
            convert_files_in_directory(path)
        elif os.path.isfile(path) and path.endswith(".mp4"):
            convert_mp4_to_mp3(path)
        else:
            print(f"Skipping '{path}': Not a valid .mp4 file or directory")


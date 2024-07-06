from moviepy.editor import VideoFileClip
import sys
import whisper

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

def transcribe_audio(audio_filepath):
    """
    Transcribes an audio file to text using Whisper.

    Parameters:
        audio_filepath (str): The path to the audio file.
    """
    model = whisper.load_model("medium")  # 'large' for better accurracy
    result = model.transcribe(audio_filepath)
    text_filepath = audio_filepath.replace(".mp3", ".txt")
    with open(text_filepath, "w") as file:
        file.write(result["text"])
    print(f"Transcribed audio to '{text_filepath}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <video_file.mp4>")
        sys.exit(1)

    video_file = sys.argv[1]
    audio_file = convert_mp4_to_mp3(video_file)
    transcribe_audio(audio_file)

import subprocess
from moviepy import VideoFileClip


def trim_video(input_path, start, end, output_path):
    print("trim_video", input_path, start, end, output_path)
    clip = VideoFileClip(input_path).subclipped(start, end)
    clip.write_videofile(output_path)
    return output_path


def remove_silence(input_path, output_path):
    print("remove_silence", input_path, output_path)
    cmd = ["ffmpeg", "-i", input_path, "-af", "silenceremove=1:0:-50dB", output_path]
    subprocess.run(cmd, check=True)
    return output_path


def add_subtitles(input_path, subtitle_file, output_path):
    print("add_subtitles", input_path, subtitle_file, output_path)
    cmd = ["ffmpeg", "-i", input_path, "-vf", f"subtitles={subtitle_file}", output_path]
    subprocess.run(cmd, check=True)
    return output_path

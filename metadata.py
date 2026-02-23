from moviepy import VideoFileClip


def extract_metadata(video_path):
    clip = VideoFileClip(video_path)
    return {"duration": clip.duration, "fps": clip.fps, "resolution": clip.size}

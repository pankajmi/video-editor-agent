import whisper


def transcribe_video(input_path, output_path):
    model = whisper.load_model("base")
    result = model.transcribe(input_path)
    print(result["text"])
    return result["text"]

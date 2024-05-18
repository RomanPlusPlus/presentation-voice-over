from pathlib import Path
from openai import OpenAI

client = OpenAI()


def text_to_speech(text, ind, mp3s_dir):
    project_root = Path(__file__).resolve().parent.parent
    speech_file_path = project_root / mp3s_dir / f"speech_{ind}.mp3"


    with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="onyx",
        input=text,
    ) as response:
        response.stream_to_file(speech_file_path)

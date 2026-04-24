from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(audio_path: str) -> str:
    """Whisper APIを使用して音声をテキストにトランスクライブ"""
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="ja"
            )
        return transcript.text
    except Exception as e:
        raise Exception(f"トランスクリプションエラー: {str(e)}")

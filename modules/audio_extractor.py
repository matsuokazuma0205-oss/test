import os
from moviepy.editor import VideoFileClip
from config import AUDIO_FORMAT, AUDIO_SAMPLE_RATE

def extract_audio(video_path: str, output_audio_path: str) -> str:
    """動画ファイルから音声を抽出"""
    try:
        video = VideoFileClip(video_path)
        audio = video.audio

        if audio is None:
            raise ValueError("動画ファイルに音声トラックが含まれていません")

        audio.write_audiofile(
            output_audio_path,
            fps=AUDIO_SAMPLE_RATE,
            verbose=False,
            logger=None
        )

        video.close()
        return output_audio_path
    except Exception as e:
        raise Exception(f"音声抽出エラー: {str(e)}")

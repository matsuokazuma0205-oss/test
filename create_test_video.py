import numpy as np
from moviepy.editor import VideoClip, ImageClip, concatenate_videoclips, AudioFileClip
from moviepy.audio.AudioFileClip import AudioFileClip
from scipy.io import wavfile
import os

def create_test_video():
    """テスト用のダミー動画を作成"""
    print("📹 テスト動画を生成中...")

    # サンプル音声を生成（440Hz の音 + スピーチパターン）
    sample_rate = 16000
    duration = 10  # 10秒

    t = np.linspace(0, duration, sample_rate * duration)
    # スピーチをシミュレート（複数の周波数を混ぜる）
    audio = (
        0.3 * np.sin(2 * np.pi * 440 * t) +  # 440Hz (A4)
        0.2 * np.sin(2 * np.pi * 550 * t) +  # 550Hz
        0.1 * np.sin(2 * np.pi * 660 * t)    # 660Hz
    )
    audio = (audio * 32767).astype(np.int16)

    # 音声ファイルを保存
    audio_path = "/tmp/test_audio.wav"
    wavfile.write(audio_path, sample_rate, audio)

    # ダミー画像を作成（黒い背景にテキスト）
    frame = np.zeros((480, 640, 3), dtype=np.uint8)

    def make_frame(t):
        return np.zeros((480, 640, 3), dtype=np.uint8)

    # ビデオクリップを作成
    video_clip = VideoClip(make_frame=make_frame, duration=duration)
    audio_clip = AudioFileClip(audio_path)
    video_clip = video_clip.set_audio(audio_clip)

    # MP4 として保存
    output_path = "test_meeting.mp4"
    video_clip.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None
    )

    print(f"✅ テスト動画を作成しました: {output_path}")
    return output_path

if __name__ == "__main__":
    create_test_video()

import numpy as np
from scipy.io import wavfile

def create_test_audio():
    """テスト用の音声ファイルを作成"""
    print("🎵 テスト音声ファイルを生成中...")

    sample_rate = 16000
    duration = 5  # 5秒

    # スピーチ的なパターンの音声を作成
    t = np.linspace(0, duration, sample_rate * duration)

    # 複数の周波数を混ぜてスピーチらしくする
    audio = (
        0.3 * np.sin(2 * np.pi * 300 * t) +      # 低音
        0.2 * np.sin(2 * np.pi * 700 * t) +      # 中音
        0.15 * np.sin(2 * np.pi * 1200 * t) +    # 高音
        0.1 * np.random.randn(len(t))             # ノイズ
    )

    # ノーマライズ
    audio = audio / np.max(np.abs(audio))
    audio = (audio * 32767).astype(np.int16)

    output_path = "test_meeting.wav"
    wavfile.write(output_path, sample_rate, audio)

    print(f"✅ テスト音声ファイルを作成しました: {output_path}")
    print(f"   サンプルレート: {sample_rate} Hz")
    print(f"   期間: {duration} 秒")

if __name__ == "__main__":
    create_test_audio()

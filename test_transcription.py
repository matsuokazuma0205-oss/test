#!/usr/bin/env python
"""トランスクリプション機能のテスト"""

from modules.transcriber import transcribe_audio

def test_transcription():
    """音声トランスクリプションをテスト"""
    print("🎵 トランスクリプション機能をテスト中...\n")

    audio_path = "test_meeting.wav"

    try:
        print(f"📝 {audio_path} をトランスクライブ中...")
        transcript = transcribe_audio(audio_path)

        print("\n✅ トランスクリプション成功！\n")
        print("=" * 50)
        print("トランスクリプション結果:")
        print("=" * 50)
        print(transcript)
        print("=" * 50)

        return transcript

    except Exception as e:
        print(f"\n❌ エラー: {str(e)}")
        return None

if __name__ == "__main__":
    test_transcription()

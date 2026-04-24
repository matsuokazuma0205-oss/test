import os
import sys
from pathlib import Path
from datetime import datetime
from modules.audio_extractor import extract_audio
from modules.transcriber import transcribe_audio
from modules.summarizer import summarize_text
from modules.key_point_extractor import extract_key_points
from config import OUTPUT_DIR, MARKDOWN_FORMAT

def create_output_dir():
    """出力ディレクトリを作成"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_markdown_notes(
    transcript: str,
    summary: str,
    key_points: list,
    video_filename: str
) -> str:
    """Markdown形式の議事録を生成"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    markdown = f"""# 議事録: {video_filename}

**作成日時**: {timestamp}

## 概要
{summary}

## 重要ポイント
"""

    for i, point in enumerate(key_points, 1):
        markdown += f"- {point}\n"

    markdown += f"""
## 詳細トランスクリプション
{transcript}
"""

    return markdown

def process_video(video_path: str) -> str:
    """動画ファイルから議事録を生成"""
    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"ファイルが見つかりません: {video_path}")

        video_filename = Path(video_path).stem

        print(f"📹 処理開始: {video_filename}")

        # ステップ1: 音声抽出
        print("🎵 音声抽出中...")
        audio_path = f"/tmp/{video_filename}_audio.wav"
        extract_audio(video_path, audio_path)

        # ステップ2: トランスクリプション
        print("📝 音声をテキストに変換中...")
        transcript = transcribe_audio(audio_path)

        # ステップ3: 要約
        print("📊 テキストを要約中...")
        summary = summarize_text(transcript)

        # ステップ4: キーポイント抽出
        print("🔑 重要ポイントを抽出中...")
        key_points = extract_key_points(transcript)

        # ステップ5: 議事録生成
        print("✍️  議事録を生成中...")
        if MARKDOWN_FORMAT:
            notes = generate_markdown_notes(transcript, summary, key_points, video_filename)
            output_path = os.path.join(OUTPUT_DIR, f"{video_filename}_notes.md")
        else:
            output_path = os.path.join(OUTPUT_DIR, f"{video_filename}_notes.txt")
            notes = f"議事録: {video_filename}\n\n概要:\n{summary}\n\n重要ポイント:\n" + "\n".join(f"- {p}" for p in key_points) + f"\n\n詳細:\n{transcript}"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(notes)

        # クリーンアップ
        if os.path.exists(audio_path):
            os.remove(audio_path)

        print(f"✅ 完了！ 議事録を保存しました: {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}", file=sys.stderr)
        raise

def main():
    """メイン処理"""
    create_output_dir()

    if len(sys.argv) < 2:
        print("使用方法: python main.py <video_file_path>")
        print("例: python main.py meeting.mp4")
        sys.exit(1)

    video_path = sys.argv[1]
    process_video(video_path)

if __name__ == "__main__":
    main()

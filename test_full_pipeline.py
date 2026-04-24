#!/usr/bin/env python
"""フル処理パイプラインのテスト（モック版）"""

from modules.summarizer import summarize_text
from modules.key_point_extractor import extract_key_points
from modules.transcriber import transcribe_audio
import os

def test_full_pipeline():
    """完全なパイプラインをテスト"""
    print("🧪 議事録生成パイプラインをテスト中...\n")

    # ダミートランスクリプト
    sample_transcript = """
    本日は新しいプロジェクトについて討議を行いました。
    プロジェクトの目標は、ユーザー体験を向上させることです。
    チームメンバーから以下の提案がありました。

    第一に、ユーザーインターフェースの改善が重要です。
    現在のUIは複雑で、ユーザーが操作に迷うことが多いです。

    第二に、パフォーマンスの最適化が必要です。
    アプリケーションの読み込み時間を短縮する必要があります。

    第三に、セキュリティ対策を強化する必要があります。
    ユーザーデータの保護が最優先事項です。

    次のステップとして、デザインチームがプロトタイプを作成します。
    開発チームは技術的な検証を行います。
    QAチームはテスト計画を準備します。

    次回のミーティングは来週予定です。
    """

    print("=" * 60)
    print("📝 トランスクリプション（テスト）")
    print("=" * 60)
    print(sample_transcript[:200] + "...\n")

    try:
        # テキスト要約
        print("📊 要約を生成中...")
        summary = summarize_text(sample_transcript)
        print("\n✅ 要約完了：\n")
        print(summary)
        print()

        # キーポイント抽出
        print("🔑 キーポイントを抽出中...")
        key_points = extract_key_points(sample_transcript)
        print("\n✅ キーポイント抽出完了：\n")
        for i, point in enumerate(key_points, 1):
            print(f"  {i}. {point}")
        print()

        # Markdown議事録を生成
        print("✍️  議事録を生成中...")
        markdown = f"""# 議事録: テスト会議

**作成日時**: 2024年テスト実行

## 概要
{summary}

## 重要ポイント
"""
        for point in key_points:
            markdown += f"- {point}\n"

        markdown += f"""
## 詳細トランスクリプション
{sample_transcript}
"""

        output_path = "test_meeting_notes.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"\n✅ 議事録を生成しました: {output_path}\n")

        print("=" * 60)
        print("テスト完了！ローカル環境で実行してください。")
        print("=" * 60)
        print("\n👉 使用方法:")
        print("   python main.py <動画ファイルパス>")
        print("\n例:")
        print("   python main.py meeting.mp4")
        print("   python main.py /path/to/screen_recording.mov")

    except Exception as e:
        print(f"\n❌ エラー: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_full_pipeline()

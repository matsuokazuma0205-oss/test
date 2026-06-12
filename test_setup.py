#!/usr/bin/env python
"""セットアップテスト - 必要なライブラリが正常にインストールされたか確認"""

import sys

def test_imports():
    """ライブラリのインポートをテスト"""
    print("🔍 ライブラリのインポートをテスト中...\n")

    libraries = [
        ("openai", "OpenAI API"),
        ("moviepy", "MoviePy (動画処理)"),
        ("scipy", "SciPy"),
        ("numpy", "NumPy"),
        ("transformers", "Hugging Face Transformers"),
        ("keybert", "KeyBERT"),
        ("dotenv", "Python-dotenv"),
    ]

    failed = []

    for lib_name, lib_display in libraries:
        try:
            __import__(lib_name)
            print(f"✅ {lib_display} - 成功")
        except ImportError as e:
            print(f"❌ {lib_display} - 失敗")
            failed.append((lib_name, str(e)))

    print("\n" + "="*50)

    if failed:
        print(f"\n⚠️  {len(failed)} 個のライブラリがインストールできていません：\n")
        for lib_name, error in failed:
            print(f"  - {lib_name}: {error}")
        return False
    else:
        print("\n✨ すべてのライブラリがインストールされました！")
        return True

def test_config():
    """設定ファイルをテスト"""
    print("\n🔍 設定をテスト中...\n")

    try:
        from config import OPENAI_API_KEY
        if OPENAI_API_KEY:
            print("✅ OpenAI API キー - 設定済み")
            return True
        else:
            print("❌ OpenAI API キー - 未設定")
            return False
    except Exception as e:
        print(f"❌ 設定ファイルの読み込み失敗: {e}")
        return False

if __name__ == "__main__":
    imports_ok = test_imports()
    config_ok = test_config()

    print("\n" + "="*50)
    if imports_ok and config_ok:
        print("\n🎉 セットアップ完了！実行可能な状態です。")
        print("\n以下のコマンドでプログラムを実行できます：")
        print("  python main.py <動画ファイルパス>")
        sys.exit(0)
    else:
        print("\n❌ セットアップに問題があります。修正してください。")
        sys.exit(1)

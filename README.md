# スクリーン録画から議事録自動生成ツール

デスクトップ上のスクリーン録画（MP4/MOV）から自動で議事録を生成するPythonツールです。

## 機能

✨ **主な機能**
- 🎥 動画ファイル（MP4/MOV など）から音声を自動抽出
- 🎵 **音声トランスクリプション**: OpenAI Whisper API を使用した高精度な音声認識
- 📝 **テキスト要約**: Facebook BART モデルによる自動要約
- 🔑 **キーポイント抽出**: KeyBERT によるキーワード自動抽出
- 📄 **Markdown 形式**: 構造化された議事録を自動生成

## 要件

- Python 3.8+
- OpenAI API キー
- 十分なディスク空き容量（動画処理用）

## インストール

```bash
# 依存ライブラリのインストール
pip install -r requirements.txt

# 環境変数を設定（.envファイルを作成）
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 使用方法

```bash
python main.py <動画ファイルパス>
```

### 例

```bash
python main.py meeting.mp4
python main.py /path/to/screen_recording.mov
```

## 出力ファイル

生成された議事録は `output/` ディレクトリに保存されます。

**出力形式（Markdown）:**
```
# 議事録: ファイル名

**作成日時**: YYYY-MM-DD HH:MM:SS

## 概要
[自動生成された要約]

## 重要ポイント
- キーワード1
- キーワード2
...

## 詳細トランスクリプション
[完全な音声認識テキスト]
```

## 処理フロー

1. 📹 動画ファイルから音声を抽出
2. 🎵 Whisper API で音声認識（日本語対応）
3. 📊 BART モデルでテキスト要約
4. 🔑 KeyBERT でキーワード抽出
5. ✍️ Markdown 形式の議事録を生成

## 設定のカスタマイズ

`config.py` で以下をカスタマイズ可能：

```python
# テキスト要約の長さ
MAX_SUMMARY_LENGTH = 150
MIN_SUMMARY_LENGTH = 50

# 抽出するキーワード数
NUM_KEYWORDS = 10

# 出力ディレクトリ
OUTPUT_DIR = "./output"
```

## トラブルシューティング

### "OPENAI_API_KEY not found" エラー
→ `.env` ファイルに OpenAI API キーを設定してください

### "Audio track not found" エラー
→ 動画ファイルに音声トラックが含まれていることを確認してください

### メモリ不足エラー
→ より小さな動画ファイルから始めるか、モデルを軽量版に変更してください

## ライセンス

MIT License

## 備考

- 初回実行時は各モデルのダウンロードに時間がかかる場合があります
- 長い動画の処理にはそれなりの時間が必要です
- 日本語での音声認識と要約に最適化されています

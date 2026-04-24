import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI Whisper API キー
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 音声抽出設定
AUDIO_FORMAT = "wav"
AUDIO_SAMPLE_RATE = 16000

# テキスト要約設定
SUMMARIZER_MODEL = "facebook/bart-large-cnn"
MAX_SUMMARY_LENGTH = 150
MIN_SUMMARY_LENGTH = 50

# キーワード抽出設定
KEYBERT_MODEL = "distiluse-base-multilingual-cased-v2"
NUM_KEYWORDS = 10

# 出力設定
OUTPUT_DIR = "./output"
MARKDOWN_FORMAT = True

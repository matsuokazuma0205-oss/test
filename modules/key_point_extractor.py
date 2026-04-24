from keybert import KeyBERT
from config import KEYBERT_MODEL, NUM_KEYWORDS

kw_model = KeyBERT(model=KEYBERT_MODEL)

def extract_key_points(text: str) -> list:
    """テキストからキーワード（重要ポイント）を抽出"""
    try:
        keywords = kw_model.extract_keywords(
            text,
            language="japanese",
            top_n=NUM_KEYWORDS,
            use_mmr=True,
            diversity=0.7
        )
        return [kw[0] for kw in keywords]
    except Exception as e:
        raise Exception(f"キーワード抽出エラー: {str(e)}")

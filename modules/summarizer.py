from transformers import pipeline
from config import SUMMARIZER_MODEL, MAX_SUMMARY_LENGTH, MIN_SUMMARY_LENGTH

summarizer = pipeline("summarization", model=SUMMARIZER_MODEL)

def summarize_text(text: str) -> str:
    """テキストを要約"""
    try:
        if len(text.split()) < 50:
            return text

        summary = summarizer(
            text,
            max_length=MAX_SUMMARY_LENGTH,
            min_length=MIN_SUMMARY_LENGTH,
            do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        raise Exception(f"要約エラー: {str(e)}")

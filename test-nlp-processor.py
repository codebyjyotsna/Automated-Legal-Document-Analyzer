import pytest
from app.utils.nlp_processor import simplify_text, summarize_text

def test_simplify_text():
    text = "This is a complex legal text that needs to be simplified for better understanding."
    simplified = simplify_text(text)
    assert isinstance(simplified, str)
    assert len(simplified) < len(text)

def test_summarize_text():
    text = "This is a long legal text that requires summarization for concise understanding."
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) < len(text)

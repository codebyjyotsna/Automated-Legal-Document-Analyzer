from transformers import pipeline

# Initialize NLP models
simplification_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def simplify_text(text):
    simplified = simplification_pipeline(text, max_length=130, min_length=30, do_sample=False)
    return simplified[0]['summary_text']

def summarize_text(text):
    summary = summarization_pipeline(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']

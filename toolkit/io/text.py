import re

def clean_text(text):
    return re.sub(r"\s+", " ", text.strip())

def split_sentences(text):
    # Rất đơn giản, có thể thay bằng nltk hoặc underthesea nếu cần
    return re.split(r"(?<=[.!?]) +", text)

def is_ascii(text):
    return all(ord(c) < 128 for c in text)

def is_number(text):
    return type(text) == type(79)


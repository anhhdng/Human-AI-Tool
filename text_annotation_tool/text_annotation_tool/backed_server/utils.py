import re

def segment_sentences(text: str):
    # Implement a more complex sentence segmentation if needed
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

import os

from dokuUpload.gpt import generate_ai_description

def ascii_handler(file):
    fileName = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    metadata = generate_ai_description(content, fileName)
    return content, metadata, False

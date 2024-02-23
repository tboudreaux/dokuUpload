from nbconvert.exporters.markdown import MarkdownExporter
import re
import hashlib

from nbconvert import MarkdownExporter, PythonExporter
import nbformat

from dokuUpload.doku import upload_media_to_dokuwiki
from dokuUpload.gpt import generate_ai_description

def make_UUID_from_hash(file):
    with open(file, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def notebook_to_markdown(filePath):
    with open(filePath, 'r', encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    mdExporter = MarkdownExporter()
    pythonExporter = PythonExporter()
    mdBody, resources = mdExporter.from_notebook_node(nb)
    UUID = make_UUID_from_hash(filePath)

    newResources = {'outputs': {}}
    for fName, byte in resources['outputs'].items():
        newName = f"media:{UUID}:{fName}"
        mdBody = re.sub(fName, newName, mdBody)
        newResources['outputs'][newName] = byte
    pythonBody, _ = pythonExporter.from_notebook_node(nb)
    return mdBody, newResources, pythonBody

def jupyter_handler(file):
    print("Using NBConvert to convert to markdown...")
    content, resources, pythonBody = notebook_to_markdown(file)
    for fName, byte in resources['outputs'].items():
        upload_media_to_dokuwiki(fName, byte)
    metadata = generate_ai_description(pythonBody, file)
    return content, metadata, True

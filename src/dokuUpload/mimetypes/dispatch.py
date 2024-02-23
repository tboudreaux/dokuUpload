from dokuUpload.mimetypes.ascii import ascii_handler
from dokuUpload.mimetypes.jupyter import jupyter_handler

EXTENSION_LOOKUP = {
        '.ipynb': jupyter_handler,
        '*': ascii_handler
        }

def get_mimetype_handler(ext):
    return EXTENSION_LOOKUP.get(ext, EXTENSION_LOOKUP['*'])

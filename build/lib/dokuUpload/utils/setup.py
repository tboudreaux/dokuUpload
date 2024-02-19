import os
from dataclasses import dataclass

@dataclass
class Config:
    API_KEY: str
    DOKU_USER: str
    DOKU_PASSWORD: str
    DOKU_URL: str

def setup() -> Config:
    """
    Get all the environment variables needed to run
    the deku wiki uploader

    Returns
    -------
    cfg : Dict
        Dictionary containing all the environment variables
        needed to run the deku wiki uploader. These include
        the API_KEY, DEKU_USER, DEKU_PASSWORD, and DEKU_URL.
    """
    API_KEY = os.environ.get('OPENAI_API_KEY_DOKU', None)
    DOKU_USER = os.environ.get('DOKU_USER', None)
    DOKU_PASSWORD = os.environ.get('DOKU_PASS', None)
    DOKU_URL = os.environ.get('DOKU_URL', None)

    if not API_KEY:
        raise ValueError('API_KEY is not set')
    if not DOKU_USER:
        raise ValueError('DOKU_USER is not set')
    if not DOKU_PASSWORD:
        raise ValueError('DOKU_PASSWORD is not set')
    if not DOKU_URL:
        raise ValueError('DOKU_URL is not set')


    cfg = {
            'API_KEY': API_KEY,
            'DOKU_USER': DOKU_USER,
            'DOKU_PASSWORD': DOKU_PASSWORD,
            'DOKU_URL': DOKU_URL
            }

    cfg = Config(**cfg)

    return cfg

CONFIG = setup()


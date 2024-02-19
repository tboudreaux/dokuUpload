import os
from typing import Dict

def setup() -> Dict:
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
    API_KEY = os.environ.get('OPEN_API_KEY_DEKU', None)
    DEKU_USER = os.environ.get('DEKU_USER', None)
    DEKU_PASSWORD = os.environ.get('DEKU_PASSWORD', None)
    DEKU_URL = os.environ.get('DEKU_URL', None)

    if not API_KEY:
        raise ValueError('API_KEY is not set')
    if not DEKU_USER:
        raise ValueError('DEKU_USER is not set')
    if not DEKU_PASSWORD:
        raise ValueError('DEKU_PASSWORD is not set')
    if not DEKU_URL:
        raise ValueError('DEKU_URL is not set')


    cfg = {
            'API_KEY': API_KEY,
            'DEKU_USER': DEKU_USER,
            'DEKU_PASSWORD': DEKU_PASSWORD,
            'DEKU_URL': DEKU_URL
            }

    return cfg


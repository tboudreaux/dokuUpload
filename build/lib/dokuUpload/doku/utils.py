import dokuwiki

from dokuUpload.utils.setup import CONFIG

def test_login():
    url = CONFIG.DOKU_URL
    username = CONFIG.DOKU_USER
    password = CONFIG.DOKU_PASSWORD
    wiki = dokuwiki.DokuWiki(url, username, password)
    return wiki.login(username, password)

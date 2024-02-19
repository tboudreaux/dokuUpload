import xmlrpc.client
from dokuUpload.utils.setup import CONFIG

def test_dokuwiki_xmlrpc(url, username, password):
    try:
        server = xmlrpc.client.ServerProxy(url)
        token = server.dokuwiki.login(username, password)
        if token:
            version = server.dokuwiki.getVersion(token)
            print(f"Successfully authenticated. DokuWiki version: {version}")
        else:
            print("Authentication failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def testLogin():
    url = CONFIG.DEKU_URL
    username = CONFIG.DEKU_USER
    password = CONFIG.DEKU_PASSWORD
    test_dokuwiki_xmlrpc(url, username, password)

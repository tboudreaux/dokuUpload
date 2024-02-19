import argparse
import os

from dokuUpload.gpt import generate_ai_description
from dokuUpload.doku import upload_to_dokuwiki
from dokuUpload.doku.utils import test_login

def main():
    parser = argparse.ArgumentParser(description="Your CLI tool description.")
    parser.add_argument('-t', '--test', action='store_true', help='Run in test mode (no files needed)')

    args,_ = parser.parse_known_args()

    if not args.test:
        parser.add_argument('files', nargs='+', help='Files to process')
    else:
        pass
    args = parser.parse_args()

    if args.test:
        print("Testing Login to dokuWiki!")
        if test_login():
            print("Login successful!")
        else:
            from dokuUpload.utils.setup import CONFIG
            print(f"Login failed! {CONFIG.DOKU_USER}@{CONFIG.DOKU_URL}")
    else:
        for file in args.files:
            assert os.path.exists(file), f'File {file} does not exist'
            print(f'Uploading {file}...')
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            metadata = generate_ai_description(content)
            upload_to_dokuwiki(content, metadata)


if __name__ == '__main__':
    main()

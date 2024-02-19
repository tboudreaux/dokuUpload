import argparse
import os

from dokuUpload.gpt import generate_ai_description
from dokuUpload.doku import upload_to_dokuwiki

def main():
    parser = argparse.ArgumentParser(description='Upload files to DokuWiki')
    parser.add_argument('files', nargs='+', help='Files to upload')

    args = parser.parse_args()
    for file in args.files:
        assert os.path.exists(file), f'File {file} does not exist'
        print(f'Uploading {file}...')
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        metadata = generate_ai_description(content)
        upload_to_dokuwiki(content, metadata)


if __name__ == '__main__':
    main()

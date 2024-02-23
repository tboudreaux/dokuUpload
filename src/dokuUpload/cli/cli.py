import argparse
import os
import pathlib

from dokuUpload.doku import upload_to_dokuwiki, test_login, check_page_exists
from dokuUpload.mimetypes import get_mimetype_handler

def main():
    # Top-level parser setup
    parser = argparse.ArgumentParser(description="Upload files to DokuWiki.")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Test subcommand
    subparsers.add_parser('test', help='Test login to DokuWiki')

    # Upload subcommand
    parser_upload = subparsers.add_parser('push', help='Upload files to DokuWiki')
    parser_upload.add_argument('files', nargs='+', help='Files to process')
    parser_upload.add_argument('-f', '--filetype', type=str,
                               help="File extension type to force use (ignore file extension and use this instead)",
                               default=None)
    parser_upload.add_argument('-o', '--overwrite', action='store_true', help='Overwrite existing pages')

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'test':
        print("Testing Login to DokuWiki!")
        if test_login():
            print("Login successful!")
        else:
            print(f"Doku Login failed! Check your configuration.")
    elif args.command == 'push':
        for file in args.files:
            file_name = os.path.basename(file)
            if check_page_exists(file_name) and not args.overwrite:
                print(f"Page {file_name} already exists.")
                continue
            assert os.path.exists(file), f'File {file} does not exist.'

            print(f'Uploading {file}...')

            mime_suffix = args.filetype if args.filetype else pathlib.Path(file).suffix
            handler = get_mimetype_handler(mime_suffix)
            content, metadata, dMarkdown = handler(file)

            upload_to_dokuwiki(content, metadata, file_name, dMarkdown)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()


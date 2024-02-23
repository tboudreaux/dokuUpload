import dokuwiki
from typing import Dict, Tuple

from dokuUpload.utils.setup import CONFIG

def upload_media_to_dokuwiki(media : str, content : bytes, force : bool = True):
    print(f"Uploading media {media} to DokuWiki...")
    wiki = dokuwiki.DokuWiki(CONFIG.DOKU_URL, CONFIG.DOKU_USER, CONFIG.DOKU_PASSWORD)
    wiki.medias.set(media, content, overwrite=force)

def format_wiki_content(file_content : str, metadata : Dict, fileName : str, dMarkdown : bool) -> Tuple[str, str]:
    page_content = f"====== {metadata['title']} ======\n"  # Level 1 heading
    page_content += f"=== {fileName} ==="
    page_content += f"\n{metadata['desc']}\n\n\n"  # Description
    if not dMarkdown:
        page_content += f"\n<code {metadata['lft']}>\n"  # Start code block
    page_content += file_content  # File content
    if not dMarkdown:
        page_content += "\n</code>\n"  # End code block

    page_id = fileName.replace(' ', '_').lower()
    return page_id, page_content

def upload_to_dokuwiki(content : str, metadata : Dict, fileName : str, dMarkdown : bool) -> bool:
    print("Uploading to DokuWiki...")
    wiki = dokuwiki.DokuWiki(CONFIG.DOKU_URL, CONFIG.DOKU_USER, CONFIG.DOKU_PASSWORD)

    pageID, pageContent = format_wiki_content(content, metadata, fileName, dMarkdown)
    wiki.pages.set(pageID, pageContent)

    return wiki.pages.get(pageID)

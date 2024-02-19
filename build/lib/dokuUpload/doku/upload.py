import dokuwiki

from dokuUpload.utils.setup import CONFIG

def format_wiki_content(file_content, metadata):
    page_content = f"====== {metadata['title']} ======\n"  # Level 1 heading
    page_content += f"\n{metadata['desc']}\n"  # Description
    page_content += f"\n<code {metadata['lft']}>\n"  # Start code block
    page_content += file_content  # File content
    page_content += "\n</code>\n"  # End code block

    page_id = metadata['title'].replace(' ', '_').lower()
    return page_id, page_content

def upload_to_dokuwiki(content, metadata, force=False):
    wiki = dokuwiki.DokuWiki(CONFIG.DOKU_URL, CONFIG.DOKU_USER, CONFIG.DOKU_PASSWORD)

    p = wiki.pages.get(metadata['title'])
    if p != '' and not force:
        print(f"Page {metadata['title']} already exists")
        return False
    
    pageID, pageContent = format_wiki_content(content, metadata)
    wiki.pages.set(pageID, pageContent)

    return wiki.pages.get(pageID)

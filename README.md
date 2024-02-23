# AI Driven page builder for DekuWiki
A tool to build pages for DekuWiki based on files
and generate summaries using AI.

# Installation
Before you install you use dokuUpload you need some enviromental
variables set

 - OPENAI_API_KEY_DOKU : Set this to your openai API key
 - DOKU_USER : set this to the username for dokuWiki
 - DOKU_PASS : set those to your users password
 - DOKU_URL : set this to the url for your instance of dokuWiki

```bash
git clone https://github.com/tboudreaux/dokuUpload.git
cd dokuUpload
pip install .
```

This will install dokuUpload. The primary part of dokuUpload is the script
for uploading and summarizing files to dokuWiki. This is called dokuUpload
and should be avalible as a shell command after installation.


# Usage
You can test if your configuration works using
```bash
dokuUpload test
```


The main usage is to store files on dokuWiki. Lets say you have a python file in the current directory called KDE.py
you could create a page about that file on dokuWiki by running the following
command

```bash
dokuUpload push KDE.py
```

There will now be a page on dokuWiki with an AI generated title and description 
along with the full contents of KDE.py. The program will attempt to figure
out what kind of file KDE.py is and run syntax highlighting on its content
accordingly.

## Jupyter Notebooks
In general dokuUpload is meant for use with plain text documents, specifically
things like scripts and plain text data files. Jupyter notebooks are a little
outside of this domain and might therefore be reasonably expected to be
excluded from dokuUpload. However, there is some logic built in to handle
these (assuming you use the standard naming where the extension is .ipynb).

dokuUpload will use nbconvert to turn the notebook into a markdown representation
and a python representation. The python representation will be passed to GPT-4 
for summarization; however, the markdown version will be whats actually embedded
into the content. Any images will be uploaded as well to a unique path based
on the SHA-1 hash of the notebook contents. 

Usage of this is the same as for any file

```bash
dokuUpload push CMDTest.ipynb
```

# Developing
I do not anticipate others will contribute to this project; however, anyone is free
to if they would like. I ask that all contributors regognize and adhear to usual
standard of conduct in any contributions.

If you would like to modify dokuUpload for use with a new file type (i.e. something
which either cannot be embedded in a code tag in dokuWiki or GPT-4 cannot directly
summarize) then you will want to introduce a new mimetype. First add the extension and
handler to the EXTENSION_LOOKUP dictionary in dispactch.py. Then impliment your custom
handler. Each handler needs to have the same interface. The handler interface takes a 
filepath and returns content, metadata, and dMarkdown. content is what will be included
in the page from the file, metadata is a dict containing a title, likeley file tupe (lft)
and a description (dft). Finally dMarkdown is a boolean which controls wheather content
will be placed in a code tag with the file type determined by the lft field in metadata
or if it will be directly embedded. If false it will be a code block, otherwise it will
be directly embedded.

For example if I wanted to add a custom mimetype for fortran files it might look like

dispatch.py
```python
from dokuUpload.mimetypes.ascii import ascii_handler
from dokuUpload.mimetypes.jupyter import jupyter_handler

EXTENSION_LOOKUP = {
        '.ipynb': jupyter_handler,
        '*': ascii_handler
        }

# These are the only two new lines I have added from what is in dispactch.py as of Feb 23 2024
from dokuUpload.mimetypes.fortran import fortran77_handler
EXTENSION_LOOKUP[".f77"] = fortran77_handler

def get_mimetype_handler(ext):
    return EXTENSION_LOOKUP.get(ext, EXTENSION_LOOKUP['*'])
```

fortran77.py
```python
import os

from dokuUpload.gpt import generate_ai_description

def fortran77_handler(file):
    fileName = os.path.basename(file)
    content = "This is a Fortran 77 File. All interpritation should be done under that lense: "
    with open(file, 'r') as f:
        content += f.read()

    metadata = generate_ai_description(content)
    return content, metadata, False
```

Now when you call <code bash>dokuUpload push</code> on any file ending with f77 the fortran77_handler will
be used.

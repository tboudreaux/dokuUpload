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
Lets say you have a python file in the current directory called KDE.py
you could create a page about that file on dokuWiki by running the following
command

```bash
dokuUpload KDE.py
```

There will now be a page on dokuWiki with an AI generated title and description 
along with the full contents of KDE.py. The program will attempt to figure
out what kind of file KDE.py is and run syntax highlighting on its content
accordingly.

import json
from openai import OpenAI
from typing import Dict

from dokuUpload.utils.setup import CONFIG


def generate_ai_description(text : str) -> Dict:
    """
    Use the GPT-4 model to generate a description of the text
    provided. This description will include a suggested title
    for a wiki page about it, likely file type, and description
    about what the file might be for. For lft only return the
    name of the type of file (for example a python file should
    return just python, whereas a .md file should just return
    markdown). Return this as a valid json string.

    Parameters
    ----------
        text : str
            The text to be summarized. This could be something
            like the contents of a python file which has been 
            read into memory.

    Returns
    -------
        response : Dict
            A dictionary containing the response from the GPT-4


    Exceptions
    ----------
        AssertionError
            If the response from the GPT-4 is None, then raise
            an AssertionError.

    Examples
    --------
    >>> generate_description("import os\nprint('Hello World')")
    Out[1]: {'desc': 'A python file that prints Hello World', 'lft': 'python', 'title': 'Hello World'}
    """
    client = OpenAI(
        api_key=CONFIG.API_KEY
    )
    response = client.chat.completions.create(
        messages = [{
            "role": "user",
            "content": f"Provide a brief description of this content including a suggested title (title) for a wiki page about it, likley file type (lft), and description (desc) about what the file might be for. For lft only return the name of the type of file (for example a python file should return just python, whereas a .md file should just return markdown). Return this as a valid json string:\n{text}",
        }],
        model="gpt-4-0125-preview", 
        response_format={'type': 'json_object'}
    )

    assert response.choices[0].message.content is not None, "No response from GPT-4"

    return json.loads(response.choices[0].message.content)

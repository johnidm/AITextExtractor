import os
import logging
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise Exception(
        "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

OPENAI_MODEL = "gpt-4o-mini"


def summarize_text(text):
    """
    Summarize the provided text using OpenAI's gpt-4o-mini model.
    
    Args:
        text (str): The text to summarize
        
    Returns:
        str: The summarized text
    
    Raises:
        Exception: If there's an error with the API call
    """
    try:
        logging.debug("Sending summarization request to OpenAI")
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{
                "role":
                "system",
                "content":
                "You are a helpful assistant that summarizes text concisely while preserving key information."
            }, {
                "role":
                "user",
                "content":
                f"Please summarize the following text in a concise manner:\n\n{text}"
            }],
            max_tokens=500)

        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error summarizing text: {str(e)}")
        raise Exception(f"Failed to summarize text: {str(e)}")


def extract_breadcrumbs(text, separator_type=None):
    """
    Extract breadcrumb trail from the provided text using OpenAI's gpt-4o-mini model.
    
    Args:
        text (str): The text to extract breadcrumbs from
        separator_type (str, optional): The type of separator to use for breadcrumbs. 
                                       Can be 'slash', 'greater_than', or None (to let OpenAI decide)
        
    Returns:
        str: The extracted breadcrumb trail
    
    Raises:
        Exception: If there's an error with the API call
    """

    try:
        logging.debug("Sending breadcrumb extraction request to OpenAI")
        
        # Determine which separator examples to include
        system_content = """You are a helpful assistant that extracts breadcrumb navigation trails from text.
        A breadcrumb is a horizontally arranged series of text links separated by either the "greater than" symbol (>) or the "forward slash" symbol (/).
        Examples:
        - Home > Clothing > Women's > Dresses
        - Home / Clothing / Women's / Dresses
        - Home > Pictures > Summer 15 Italy
        - Home / Pictures / Summer 15 Italy
        Extract or create the most relevant breadcrumb trail based on the content of the text. You can use either separator style."""
        
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{
                "role": "system",
                "content": system_content
            }, {
                "role": "user",
                "content": f"Extract or create a relevant breadcrumb trail from the following text:\n\n{text}"
            }],
            max_tokens=200)

        # Get the raw response
        breadcrumb_trail = response.choices[0].message.content.strip()
        
        # If a specific separator type is requested, ensure the response uses that separator
        if separator_type == "slash" and ">" in breadcrumb_trail:
            # Convert greater than to forward slash
            breadcrumb_trail = breadcrumb_trail.replace(" > ", " / ")
        elif separator_type == "greater_than" and "/" in breadcrumb_trail:
            # Convert forward slash to greater than
            breadcrumb_trail = breadcrumb_trail.replace(" / ", " > ")
            
        return breadcrumb_trail
    except Exception as e:
        logging.error(f"Error extracting breadcrumbs: {str(e)}")
        raise Exception(f"Failed to extract breadcrumbs: {str(e)}")

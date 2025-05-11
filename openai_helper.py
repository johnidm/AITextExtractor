import os
import logging
from openai import OpenAI

# Get API key from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

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
    if not OPENAI_API_KEY:
        raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        logging.debug("Sending summarization request to OpenAI")
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using the specified model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text concisely while preserving key information."},
                {"role": "user", "content": f"Please summarize the following text in a concise manner:\n\n{text}"}
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error summarizing text: {str(e)}")
        raise Exception(f"Failed to summarize text: {str(e)}")

def extract_breadcrumbs(text):
    """
    Extract breadcrumb trail from the provided text using OpenAI's gpt-4o-mini model.
    
    Args:
        text (str): The text to extract breadcrumbs from
        
    Returns:
        str: The extracted breadcrumb trail
    
    Raises:
        Exception: If there's an error with the API call
    """
    if not OPENAI_API_KEY:
        raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        logging.debug("Sending breadcrumb extraction request to OpenAI")
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using the specified model
            messages=[
                {"role": "system", "content": """You are a helpful assistant that extracts breadcrumb navigation trails from text.
                A breadcrumb is a horizontally arranged series of text links separated by the "greater than" symbol (>).
                Examples:
                - Home > Clothing > Women's > Dresses
                - Home > Pictures > Summer 15 Italy
                Extract or create the most relevant breadcrumb trail based on the content of the text."""},
                {"role": "user", "content": f"Extract or create a relevant breadcrumb trail from the following text:\n\n{text}"}
            ],
            max_tokens=200
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Error extracting breadcrumbs: {str(e)}")
        raise Exception(f"Failed to extract breadcrumbs: {str(e)}")

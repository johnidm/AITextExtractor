# Text Analyzer

A powerful web application that uses OpenAI's gpt-4o-mini model to analyze text, providing concise summaries and extracting breadcrumb trails.

## Features

- **Text Summarization**: Automatically condenses lengthy text into concise summaries while preserving key information.
- **Breadcrumb Trail Extraction**: Identifies or creates a hierarchical breadcrumb trail from the content with support for both separator styles:
  - Forward slash format: `Home / Category / Subcategory`
  - Greater than format: `Home > Category > Subcategory`
- **Custom Separator Selection**: Users can choose their preferred breadcrumb separator style with the click of a button.
- **Responsive UI**: Clean, modern interface built with Bootstrap that works on both desktop and mobile devices.
- **Real-time Processing**: Processes text in real-time using OpenAI's powerful language models.

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript with Bootstrap framework
- **AI**: OpenAI's gpt-4o-mini model
- **Deployment**: Hosted on Replit

## How to Use

1. Visit the application's homepage.
2. Enter or paste the text you want to analyze in the text area.
3. Click the "Process Text" button.
4. Wait for the AI to process your text (typically takes a few seconds).
5. View the generated summary and breadcrumb trail in the results section.

## Setup Requirements

To run this application locally, you need:

1. Python 3.10 or higher
2. An OpenAI API key (set as environment variable `OPENAI_API_KEY`)
3. Required Python packages (see `pyproject.toml`)

## Installation Instructions

1. Clone the repository
2. Set up a virtual environment (optional but recommended)
3. Install dependencies: `pip install -r requirements.txt` (or use the package manager of your choice)
4. Set your OpenAI API key as an environment variable
5. Run the application: `python main.py`

## Configuration

The application uses the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for authentication
- `SESSION_SECRET`: Secret key for Flask sessions (optional, defaults to a development key)
- `PORT`: Port to run the server on (defaults to 5000)

## License

MIT License

## Contributions

Contributions, issues, and feature requests are welcome!

## Acknowledgements

- OpenAI for providing the AI models
- Bootstrap for the UI framework
import os
import logging
from flask import Flask, render_template, request, jsonify
from services import summarize_text, extract_breadcrumbs

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_text():
    """Process the submitted text and return summary and breadcrumbs."""
    data = request.json if request.json else {}
    text = data.get('text', '')
    separator_type = data.get('separator_type')  # Get separator preference if provided

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Get text summary from OpenAI
        summary = summarize_text(text)

        # Extract breadcrumbs from text with optional separator type
        breadcrumbs = extract_breadcrumbs(text, separator_type)

        return jsonify({'summary': summary, 'breadcrumbs': breadcrumbs})
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

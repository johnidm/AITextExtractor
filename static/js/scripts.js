document.addEventListener('DOMContentLoaded', function() {
    const textForm = document.getElementById('textForm');
    const inputText = document.getElementById('inputText');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    const resultsSection = document.getElementById('resultsSection');
    const summaryResult = document.getElementById('summaryResult');
    const breadcrumbsResult = document.getElementById('breadcrumbsResult');

    // Form submission handler
    textForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get the input text
        const text = inputText.value.trim();
        
        // Validate input
        if (!text) {
            showError('Please enter some text to analyze.');
            return;
        }
        
        // Show loading indicator
        showLoading(true);
        hideError();
        hideResults();
        
        // Send the request to the backend
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'An unknown error occurred');
                });
            }
            return response.json();
        })
        .then(data => {
            // Hide loading indicator
            showLoading(false);
            
            // Display results
            displayResults(data);
        })
        .catch(error => {
            // Hide loading indicator
            showLoading(false);
            
            // Show error message
            showError(error.message || 'An error occurred while processing your request');
        });
    });

    // Function to show/hide loading indicator
    function showLoading(show) {
        if (show) {
            loadingIndicator.classList.remove('d-none');
        } else {
            loadingIndicator.classList.add('d-none');
        }
    }

    // Function to show error message
    function showError(message) {
        errorMessage.textContent = message;
        errorAlert.classList.remove('d-none');
    }

    // Function to hide error message
    function hideError() {
        errorAlert.classList.add('d-none');
    }

    // Function to display results
    function displayResults(data) {
        // Set the summary text
        summaryResult.textContent = data.summary;
        
        // Set the breadcrumbs text
        breadcrumbsResult.textContent = data.breadcrumbs;
        
        // Show the results section
        resultsSection.classList.remove('d-none');
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    // Function to hide results
    function hideResults() {
        resultsSection.classList.add('d-none');
    }
});

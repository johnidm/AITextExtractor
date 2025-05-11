document.addEventListener('DOMContentLoaded', function() {
    const textForm = document.getElementById('textForm');
    const inputText = document.getElementById('inputText');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    const resultsSection = document.getElementById('resultsSection');
    const summaryResult = document.getElementById('summaryResult');
    const breadcrumbsResult = document.getElementById('breadcrumbsResult');
    const separatorButtons = document.querySelectorAll('.separator-btn');
    
    // Store the original breadcrumbs response
    let originalBreadcrumbs = '';
    
    // Current separator preference
    let currentSeparator = 'default';

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
        
        // Reset separator buttons
        resetSeparatorButtons();
        
        // Show loading indicator
        showLoading(true);
        hideError();
        hideResults();
        
        // Get separator preference if user selected one
        const separatorBtn = document.querySelector('.separator-btn.active');
        const separatorType = separatorBtn ? 
            (separatorBtn.dataset.separator !== 'default' ? separatorBtn.dataset.separator : null) : 
            null;
            
        // Send the request to the backend
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                text: text,
                separator_type: separatorType 
            })
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
            
            // Store original breadcrumbs
            originalBreadcrumbs = data.breadcrumbs;
            
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
    
    // Separator button click handler
    separatorButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Skip if already active or no results available
            if (this.classList.contains('active') || originalBreadcrumbs === '') {
                return;
            }
            
            // Update active button
            separatorButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Get separator preference
            currentSeparator = this.dataset.separator;
            
            // Format breadcrumbs based on separator preference
            formatBreadcrumbs(currentSeparator);
        });
    });
    
    // Function to reset separator buttons
    function resetSeparatorButtons() {
        separatorButtons.forEach(btn => btn.classList.remove('active'));
        document.querySelector('[data-separator="default"]').classList.add('active');
        currentSeparator = 'default';
    }
    
    // Function to format breadcrumbs based on separator preference
    function formatBreadcrumbs(separator) {
        if (!originalBreadcrumbs) return;
        
        let formattedBreadcrumbs = originalBreadcrumbs;
        
        if (separator === 'greater_than') {
            // Replace all forward slashes with greater than
            formattedBreadcrumbs = originalBreadcrumbs.replace(/ \/ /g, ' > ');
        } else if (separator === 'slash') {
            // Replace all greater than with forward slashes
            formattedBreadcrumbs = originalBreadcrumbs.replace(/ > /g, ' / ');
        }
        
        // Display formatted breadcrumbs
        breadcrumbsResult.textContent = formattedBreadcrumbs;
    }

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
        
        // Store original breadcrumbs
        originalBreadcrumbs = data.breadcrumbs;
        
        // Show the results section
        resultsSection.classList.remove('d-none');
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    // Function to hide results
    function hideResults() {
        resultsSection.classList.add('d-none');
        originalBreadcrumbs = '';
    }
});

// scripts.js

function suggestCountryCodes() {
    const query = document.getElementById('country-code').value.toLowerCase();
    const suggestions = [
        { code: '+1', country: 'USA', flag: 'us.png' },
        { code: '+254', country: 'Kenya', flag: 'kenya.png' },
        { code: '+44', country: 'UK', flag: 'uk.png' },
        // Add more country codes here...
    ];

    const filteredSuggestions = suggestions.filter(s => s.code.includes(query) || s.country.toLowerCase().includes(query));
    const suggestionsContainer = document.getElementById('suggestions');
    suggestionsContainer.innerHTML = '';

    filteredSuggestions.forEach(suggestion => {
        const suggestionElement = document.createElement('div');
        suggestionElement.classList.add('suggestion');
        suggestionElement.innerHTML = `<img src="flags/${suggestion.flag}" alt="${suggestion.country} Flag"> ${suggestion.code} - ${suggestion.country}`;
        suggestionsContainer.appendChild(suggestionElement);
    });
}

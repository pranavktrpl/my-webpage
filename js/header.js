// js/header.js

// Function to include HTML snippets
function includeHTML() {
    const elements = document.querySelectorAll('[data-include]');
    elements.forEach(el => {
      const file = el.getAttribute('data-include');
      fetch(file)
        .then(response => response.text())
        .then(data => {
          el.innerHTML = data;
        })
        .catch(error => {
          el.innerHTML = `<p>Error loading ${file}</p>`;
          console.error('Error fetching include file:', error);
        });
    });
  }
  
  // Call the function on page load
  document.addEventListener('DOMContentLoaded', includeHTML);
  
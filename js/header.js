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
          
          // After header is loaded, update the navigation links
          if (file === 'header.html') {
            // Wait a bit to make sure the DOM is updated
            setTimeout(updateNavigationLinks, 100);
          }
        })
        .catch(error => {
          el.innerHTML = `<p>Error loading ${file}</p>`;
          console.error('Error fetching include file:', error);
        });
    });
  }
  
  // Function to update navigation links
  function updateNavigationLinks() {
    const basePath = window.basePath || '';
    document.querySelectorAll('#navigation-links a').forEach(link => {
      const page = link.getAttribute('data-page');
      // Only update if the data-page attribute exists
      if (page) {
        link.href = basePath + '/' + page;
      }
    });
  }
  
  // Call the function on page load
  document.addEventListener('DOMContentLoaded', includeHTML);
  
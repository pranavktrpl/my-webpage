document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    const confirmationMessage = document.getElementById("confirmation-message");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Submit the form using Formspree's API
        fetch("https://formspree.io/f/YOUR_FORM_ID", {
            method: "POST",
            body: new FormData(form),
            headers: {
                Accept: "application/json",
            },
        })
            .then((response) => {
                if (response.ok) {
                    // Show the confirmation message
                    confirmationMessage.style.display = "block";
                    confirmationMessage.innerText = "Thank you for your message! I will get back to you soon.";
                    form.reset(); // Clear the form
                } else {
                    confirmationMessage.style.display = "block";
                    confirmationMessage.style.color = "red";
                    confirmationMessage.innerText = "Oops! Something went wrong. Please try again.";
                }
            })
            .catch(() => {
                confirmationMessage.style.display = "block";
                confirmationMessage.style.color = "red";
                confirmationMessage.innerText = "Oops! Something went wrong. Please try again.";
            });
    });
});

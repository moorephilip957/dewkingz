document.addEventListener("DOMContentLoaded", () => {

  const button = document.querySelector(".sign-btn");
  const form = document.getElementById("validation-form");

  if (button && form) {

    button.addEventListener("click", function(event) {

      event.preventDefault();

      // Disable button
      button.disabled = true;

      // Show spinner
      button.innerHTML = `
        <span class="spinner-border spinner-border-sm me-2"></span>
        Signing in...
      `;

      // Submit form after short delay
      setTimeout(() => {

        form.submit();

      }, 200);

    });

  }

});
function validateForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');

    // Default usernames and passwords
    const validCredentials = {
        "deepak": "deepak123",
        "disha": "disha123",
        "shravani": "shravani123"
    };

    // Check if the username exists and if the password matches
    if (validCredentials[username] && validCredentials[username] === password) {
        message.textContent = "Login successful!";
        message.style.color = "green";

        // Redirect to form/form.html after successful login
        window.location.href = "form/form.html";
        return false; // Prevent default form submission
    } else {
        message.textContent = "Invalid username or password.";
        message.style.color = "red";
        return false; // Prevent form submission on invalid credentials
    }
}

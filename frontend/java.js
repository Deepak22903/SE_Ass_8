function validateForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');

    // Simple validation for demonstration
    if (username === "admin" && password === "password") {
        message.textContent = "Login successful!";
        message.style.color = "green";
        return true; // You can proceed with the login
    } else {
        message.textContent = "Invalid username or password.";
        return false; // Prevent form submission
    }
}

$(document).ready(function() {
    $('body').fadeIn(800); // Fade-in effect for the body

    function validateForm(form) {
        $('.error').remove(); // Clear previous errors
        var email = $('#emailInput').val();
        var password = $(form).find('input[type="password"]').val();
        var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        var passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{6,}$/;
        var hasError = false;

        // Debugging output
        console.log("Email: ", email);
        console.log("Password: ", password);

        if (!emailRegex.test(email)) {
            $('<span class="error">Email must be a valid address.</span>')
                .css({ color: 'red', marginLeft: '10px' })
                .insertAfter($(form).find('input[type="email"]'));
            hasError = true;
        } else {
            console.log("Email valid");
        }

        if (!passwordRegex.test(password)) {
            $('<span class="error">Password must be at least 6 characters, include one uppercase, one number, and one special character.</span>')
                .css({ color: 'red', marginLeft: '10px' })
                .insertAfter($(form).find('input[type="password"]'));
            hasError = true;
        } else {
            console.log("Password valid");
        }

        return !hasError; // Return true if no errors were found (form is valid)
    }

    $('#signUpForm').submit(function(event) {
        if (!validateForm(this)) {
            event.preventDefault();
            console.log("Form validation failed");
        } else {
            console.log("Form validation passed");
        }
    });
});

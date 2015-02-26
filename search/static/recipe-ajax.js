function showLogin(evt) {
    $("#login-text").load("/login");
}

$('#login_button').on('click', showLogin);

function showRegister(evt) {
    $("#register-text").load("/register");
}

$('#register_button').on('click', showRegister);
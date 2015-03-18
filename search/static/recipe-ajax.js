$("#login-button").on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("/login_form/");
});

$('#register-button').on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("register_form/");
});

$('#about-button').on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("about_page/");
});

$('#register-button').on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("register_form/");
});

$("#search-button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("search_page/");
});

$("#my-recipes-button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("my_recipes/");
});

$("#planner-button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("planner/");
});

$("#shopping-list-button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("shopping_list/");
});
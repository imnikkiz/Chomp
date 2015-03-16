$("#login_button").on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("/login_form/");
});

$('#register_button').on('click', function(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("register_form/");
});

$("#search_button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("search_page/");
});

$("#my_recipes_button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("my_recipes/");
});

$("#planner_button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("planner/");
});

$("#shopping_list_button").on('click', function(evt) {
    evt.preventDefault();
    $("#content").load("shopping_list/");
});
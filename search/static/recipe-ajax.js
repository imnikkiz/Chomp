function showLogin(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("/login_form/");
}

function showRegister(evt) {
    evt.preventDefault();
    $("#auth-modal").modal();
    $("#auth-modal-body").load("register_form/");
}
function showSearch(evt) {
    evt.preventDefault();
    $("#content").load("search_page/");
}
function showMyRecipes(evt) {
    evt.preventDefault();
    $("#content").load("my_recipes/");
}
function showPlanner(evt) {
    evt.preventDefault();
    $("#content").load("planner/");
}
function showShoppingList(evt) {
    evt.preventDefault();
    $("#content").load("shopping_list/");
}


$("#login_button").on('click', showLogin);
$('#register_button').on('click', showRegister);
$("#search_button").on('click', showSearch);
$("#my_recipes_button").on('click', showMyRecipes);
$("#planner_button").on('click', showPlanner);
$("#shopping_list_button").on('click', showShoppingList);
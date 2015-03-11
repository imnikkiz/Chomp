function showLogin(evt) {
    $("#content").load("login/");
}
function showRegister(evt) {
    $("#content").load("register_form/");
}
function showSearch(evt) {
    $("#content").load("search/");
}
function showMyRecipes(evt) {
    $("#content").load("my_recipes/");
}
function showPlanner(evt) {
    $("#content").load("planner/");
}
function showShoppingList(evt) {
    $("#content").load("shopping_list/");
}


$("#login_button").on('click', showLogin);
$('#register_button').on('click', showRegister);
$("#search_button").on('click', showSearch);
$("#my_recipes_button").on('click', showMyRecipes);
$("#planner_button").on('click', showPlanner);
$("#shopping_list_button").on('click', showShoppingList);

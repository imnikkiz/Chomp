angular.module("homeRoutingApp", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                template: '<h1>Hi!</h1>' })
            .when('/login', {
                templateUrl: 'login' })
            .when('/register', {
                templateUrl: 'register'});
        });

angular.module("recipeRoutingApp", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/search_page', {
                templateUrl: 'search_page' })
            .when('/my_recipes', {
                templateUrl: 'my_recipes' })
            .when('/planner', {
                templateUrl: 'planner'})
            .when('/shopping_list', {
                templateUrl: 'shopping_list'});
        });
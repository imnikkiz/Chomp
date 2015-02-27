angular.module("homeRoute", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                template: '<h1>Hi!</h1>' })
            .when('/login', {
                templateUrl: 'login' })
            .when('/register', {
                templateUrl: 'register'});
        });

angular.module("recipeRoute", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/my_recipes', {
                templateUrl: 'my_recipes' })
            .when('/search', {
                templateUrl: 'search_page' })
            .when('/planner', {
                templateUrl: 'planner'})
            .when('/shopping_list', {
                templateUrl: 'shopping_list'});
        });
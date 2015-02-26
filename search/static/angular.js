angular.module("demoApp", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                template: '<h1>Hi!</h1>' })
            .when('/login', {
                templateUrl: 'login' })
            .when('/register', {
                template: 'register.html'});
        });
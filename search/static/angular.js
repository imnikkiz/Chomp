angular.module("demoApp", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                template: '<h1>Hi!</h1>' })
            .when('/login', {
                templateURL: 'login.html' })
            .when('/register', {
                templateURL: 'register.html'});
        });
angular.module("homeRoute", ['ngRoute'])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                template: '<h1>Hi!</h1>' })
            .when('/login', {
                templateUrl: 'login' })
            .when('/register', {
                templateUrl: 'register'});
        })

    .controller("loginCtrl", ['$http', function($http){
        var self = this;
        self.login = function() {
            console.log(self.user);
//             $http({
//     method: 'POST',
//     url: '/login/',
//     data: "message=" + 'kitten',
//     headers: {'Content-Type': 'application/x-www-form-urlencoded'}
// });
            // $http.post('/login/', '{"a":"b"}');
            $http.post('/login/', self.user);
        };
    }]);

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
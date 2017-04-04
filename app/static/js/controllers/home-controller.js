(function () {
    'use strict';

    angular
        .module('lyrical')
        .controller('HomeCtrl', HomeCtrl);

    HomeCtrl.$inject = ['$scope', '$state', '$http'];

    function HomeCtrl($scope, $state, $http) {
        console.log("HomeCtrl");

        $http.get('/api').then(function(response) {
            console.log("response:");
            console.log(response);
        });

    }
}());
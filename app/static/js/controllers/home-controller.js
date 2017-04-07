(function () {
    'use strict';

    angular
        .module('lyrical')
        .controller('HomeCtrl', HomeCtrl);

    HomeCtrl.$inject = ['$scope', '$state', '$http'];

    function HomeCtrl($scope, $state, $http) {
        console.log("HomeCtrl");
        $scope.loading = false;
        $scope.search = function () {
            $scope.loading = true;
            console.log($scope.loading);
            $http.get('/api').then(function (response) {
                console.log("response:");
                console.log(response);
                $scope.loading = false;
                //$state.go('result-screen', {result: response});
            });
        };


    }
}());
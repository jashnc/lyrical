(function () {
    'use strict';

    angular
        .module('lyrical')
        .controller('SearchResultsCtrl', SearchResultsCtrl);

    SearchResultsCtrl.$inject = ['$scope', '$state', '$http', '$stateParams'];

    function SearchResultsCtrl($scope, $state, $http, $stateParams) {
        $scope.home = function() {
            $state.go('main');
        }
        console.log("SearchResultsCtrl");
        console.log($state.params);
        $scope.searchResults = $state.params.result;
        console.log($scope.searchResults);
        //$scope.searchResults = [{songTitle: "DG's Butthole", artist: "Lushwick", lyrics: "I am gay."}, {songTitle: "Jon's Butthole", artist: "Grige", lyrics: "I am gays. \n fag"}];
        
    


    }
}());
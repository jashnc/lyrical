(function () {
    'use strict';

    angular
        .module('lyrical')
        .controller('HomeCtrl', HomeCtrl);

    HomeCtrl.$inject = ['$scope', '$state', '$http'];

    function HomeCtrl($scope, $state, $http) {
        console.log("HomeCtrl");
        $scope.loading = false;
        $scope.searchType = "mood";
        $scope.artist = "";
        $scope.title = "";
        $scope.mood = "";
        $scope.search = function () {
            $scope.loading = true;
            if($scope.searchType === "mood") {
                searchMood();
            }
            else {
                searchSong();
            }
        };

        function searchMood() {
            console.log($scope.mood);
            var data = {'mood': $scope.mood};
            $http.post('/api/mood', JSON.stringify(data))
                .then(function(response) {
                    $scope.loading = false;
                    console.log(response);
                    $state.go('searchResults',{result: response.data})
                });
        }

        function searchSong() {
            var data = {title: $scope.title, artist: $scope.artist};
            $http.get('/api/title', data)
                .then(function(response) {
                    $scope.loading = false;
                    console.log(response);
                    $state.go('searchResults',{result: response.data})
                });

        }


    }
}());
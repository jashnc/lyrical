'use strict';

angular
    .module('lyrical.config', [])
    .config(['$stateProvider', '$urlRouterProvider',

    function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('main', {
                url: '/',
                templateUrl: '../static/views/home-view.html',
                controller: 'HomeCtrl'
            })
            .state('searchResults', {
                url: '/searchResults',
                params: {
                    result: null
                },
                templateUrl: '../static/views/search-results-view.html',
                controller: 'SearchResultsCtrl'
            });

    }]);
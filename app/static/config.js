'use strict';

angular
    .module('lyrical.config', [])
    .config(['$stateProvider', '$urlRouterProvider',

    function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '../static/views/home-view.html',
                controller: 'HomeCtrl'
            });

    }]);
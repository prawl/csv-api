'use strict';

angular.module('clientApp', ['restangular']);

angular.module('clientApp')
  .controller('MainCtrl', function ($scope) {
    $scope.todos = [
      'Create Django models',
      'Expose them through a REST API',
      'Consume them with restangular'
    ];
  });

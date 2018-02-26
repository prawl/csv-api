'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, Restangular) {
    Restangular.setBaseUrl('http://localhost:8000/api/');
    $scope.import_rows = Restangular.all('rows').getList().$object;
  });

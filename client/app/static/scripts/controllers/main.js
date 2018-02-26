'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, Restangular, $http, $window, $location) {
    // TODO: This should go in the configs file
    Restangular.setBaseUrl('http://localhost:8000/api/');
    $scope.import_rows = Restangular.all('rows').getList().$object;

    $scope.uploadFile = function (files) {
      var fd = new FormData();
      fd.append("file", files[0]);
      $http.post('http://localhost:8000/api/files/upload', fd, {
          withCredentials: false,
          headers: {'Content-Type': undefined },
          transformRequest: angular.identity
      }).success( $window.location.reload() );
    };
  });

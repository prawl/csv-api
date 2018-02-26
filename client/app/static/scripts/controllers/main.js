'use strict';

angular.module('clientApp')
  .controller('MainCtrl', function ($scope, Restangular, $http, $window) {
    // TODO: This should go in the configs file
    Restangular.setBaseUrl('http://localhost:8000/api/');
    $scope.import_rows = Restangular.all('rows').getList().$object;
    console.log($scope.import_rows);

    $scope.uploadFile = function (files) {
      console.log("UPLOAD!", files);
      if(files === undefined) {
        console.log("NO FILE FOUND!");
      } 
      var fd = new FormData();
      //Take the first selected file
      // debugger;
      fd.append("file", files[0]);
      $http.post('http://localhost:8000/api/files/upload', fd, {
          withCredentials: false,
          headers: {'Content-Type': undefined },
          transformRequest: angular.identity
      }).success( $window.location.reload() ).error( "oh no" );
    };
  });

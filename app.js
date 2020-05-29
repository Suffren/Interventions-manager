angular.module('app', [])

.controller('mainCtrl', function($http) {
    self = this;
    self.reports = [];

    $http.get("http://127.0.0.1:5000/api/v1/reports").then(function(res) {
        self.reports = res.data;
    });
});
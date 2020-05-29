angular.module('app', [])

.controller('mainCtrl', function(API) {
    self = this;
    self.reports = [];

    API.get('/reports').then(
        function(res) {
            self.reports = res;
        },
        function(error) {
            alert(error);
        }
    );

})
.service('API', function($http) {
    var URL = "http://127.0.0.1:5000/api/v1";

    this.get = function(URI) {
        return $http({
            method: 'GET',
            url: URL + URI
        }).then(function successCallback(response) {
            if(response.status === 200) {
                return response.data;
            } else {
                throw new Error("Une erreur est survenue.");
            }
        }, function errorCallback(response) {
            // TODO: Redirect to 404 ?
            if (response.status) {
               console.warn( response.data.error || "Server error");
               return;
            }
            // TODO: send the error to the devs
            console.error('Angular error: ', response);
        });
    }
});
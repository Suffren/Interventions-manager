angular.module('app')

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

    this.post = function(URI, data) { // Data must be an object, TODO: handle arrays
        return $http({
            method: 'POST',
            url: URL + URI,
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            transformRequest: function(obj) {
                if (obj && obj.constructor === Object) {
                    /*  Converts an object to URL parameter(s)
                    This function only works with objects */
                    return Object.keys(obj).map(function(key) {
                        return encodeURIComponent(key) + '=' + encodeURIComponent(obj[key]);
                    }).join('&');
                }
            },
            data: data
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
})
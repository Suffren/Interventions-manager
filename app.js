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
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
.component('modalIntervention', {
    templateUrl: 'modal.html',
    controller: function (API) {
        var ctrl = this;
    }
});
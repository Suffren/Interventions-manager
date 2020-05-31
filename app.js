angular.module('app', [])

.controller('mainCtrl', function(API) {
    ctrl = this;
    ctrl.reports = [];

    ctrl.showModal = false;

    ctrl.openModal = function() {
        ctrl.showModal = true;
    }

    ctrl.closeModal = function() {
        getReports();
        ctrl.showModal = false;
    }

    function getReports() {
        API.get('/reports').then(
            function(res) {
                ctrl.reports = res;
            },
            function(error) {
                alert(error);
            }
        );
    }
    getReports();
})
.component('modalIntervention', {
    templateUrl: 'modal.html',
    bindings: {
        id: '@',
        onConfirm: '&'
    },
    controller: function () {
        var ctrl = this;

        ctrl.confirm = function() {
            ctrl.onConfirm();
        }

        ctrl.cancel = function() {
            ctrl.onConfirm();
        }
    }
});
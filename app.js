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

    API.get('/reports').then(
        function(res) {
            ctrl.reports = res;
        },
        function(error) {
            alert(error);
        }
    );
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
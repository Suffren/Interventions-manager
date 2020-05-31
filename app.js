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

    ctrl.delete = function(report_id) {
        API.post('/delete_report' + '?id=' + report_id).then(
            function() {
                getReports();
            },
            function(error) {
                alert(error);
            }
        );
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
    controller: function (API) {
        var ctrl = this;

        ctrl.confirm = function() {
            API.post('/add_report', ctrl.form).then(
                function(res) {
                    ctrl.onConfirm();
                },
                function(error) {
                    alert(error);
                }
            );
        }

        ctrl.cancel = function() {
            ctrl.onConfirm();
        }
    }
});
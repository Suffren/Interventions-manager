angular.module('app', [])

.controller('mainCtrl', function(API, Modal) {
    ctrl = this;
    ctrl.reports = [];
    ctrl.reverseDateOrder = true;

    ctrl.showModal = false;

    ctrl.openModal = function(data) {
        ctrl.showModal = true;
        Modal.open(data).then(
            function(res) {
                getReports();
                ctrl.showModal = false;
            },
            function(res) {
                ctrl.showModal = false;
            }
        );
    }

    ctrl.sortByDate = function() {
        ctrl.reverseDateOrder = !ctrl.reverseDateOrder;
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
    controller: function (API, Modal) {
        var ctrl = this;
        var report = Modal.data;

        // Fill the inputs
        if(report) {
            API.get('/report' + '?id=' + Modal.data.report_id).then(
                function(res) {
                    ctrl.form = res;
                },
                function(error) {
                    alert(error);
                }
            );
        }

        ctrl.confirm = function() {
            if(report) {
                ctrl.update(ctrl.form, Modal.data.report_id);
            } else {
                ctrl.create(ctrl.form);
            }
        }

        ctrl.create = function(form) {
            API.post('/add_report', form).then(
                function(res) {
                    Modal.close();
                },
                function(error) {
                    alert(error);
                }
            );
        }

        ctrl.update = function(data, report_id) {
            API.post('/update_report' + '?id=' + report_id, data).then(
                function() {
                    Modal.close();
                },
                function(error) {
                    alert(error);
                }
            );
        }

        ctrl.cancel = function() {
            Modal.cancel()
        }
    }
});
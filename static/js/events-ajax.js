$(document).ready(function() {
    $('#nextStep').click(function() {
        $('#step1').hide();
        $('#step2').show();
    });

    $('#previousStep').click(function() {
        $('#step2').hide();
        $('#step1').show();
    });

    var successMessage = $("#jq-notification");



















    var notification = $("#notification");
    if(notification.length > 0){
        setTimeout(function(){
            notification.alert('close')
        },7000)
    }

});
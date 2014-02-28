$(document).ready(function() {

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/suggest_job/', {suggestion: query}, function(data){
            $('#job_area').html(data);
        });
    });

});

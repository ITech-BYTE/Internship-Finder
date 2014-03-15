$(document).ready(function() {

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/suggest_job/', {suggestion: query}, function(data){
            $('#job_area').html(data);
        });
    });

    $('#skill_dropdown').change(function(){
        var query;
        query = $(this).val();
        $.get('/company/suggest_intern/', {skill_1: query}, function(data){
            $('#intern_area').html(data);
        });
    });

    $('#reglist').slimScroll({
        color: '#00f',
        size: '10px',
        height: '100px',
        alwaysVisible: true
    });

    $('.bxslider').bxSlider({
        auto: true,
        mode: 'fade',
        captions: false,
        pager: false,
        controls: false,
        adaptive: true,

        autoControls: false
    });
});


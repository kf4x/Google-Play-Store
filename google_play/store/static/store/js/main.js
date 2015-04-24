$(function(){

    $("#search-btn").click(function(){

        if($('#forsearch').is(":visible")){
            if($('#forsearch').val() == ''){
                $('#forsearch').fadeOut();
                return;
            }
            $("#search-form").submit()
        } else{
            $('#forsearch').fadeIn()
        }
        return;
    });

    $('#forsearch').focusout(function() {
        $('#forsearch').fadeOut();
        return;
    });

});
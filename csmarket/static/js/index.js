/**
 * Created by thinkgamer on 17-3-9.
 */
$(document).ready(function() {
    $(window).scroll(function(){
        var top=$(window).scrollTop();
        if(top>=502){
            $("#headertop").addClass("fix");
            $("#headertop").css({color:"red",top:0});
        }else{
            $("#headertop").removeClass("fix");}
    });
});



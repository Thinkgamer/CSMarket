/**
 * Created by Administrator on 2017-05-01.
 */
$(document).ready(function(){
    $("#xcmain").particleground({
        dotColor: '#ffff00',
        lineColor: '#999999'
    });
    $("#weixinbtn").bind(
        {"mouseover":function(){
            $(".xclinkmethod>img").css("visibility","visible");
        },
        "mouseout":function(){
            $(".xclinkmethod>img").css("visibility","hidden");
        }}
    );
    $("#telbtn").bind(
        {"mouseover":function(){
            $(".xclinkmethod>p").css("visibility","visible");
        },
            "mouseout":function(){
                $(".xclinkmethod>p").css("visibility","hidden");
            }}
    );
});
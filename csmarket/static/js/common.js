/**
 * Created by Administrator on 2017-03-05.
 */
$(function(){
    $(".page-list li").click(function(){
        $(this).addClass("active").siblings().removeClass("active");
    });
    $("#mynav li").click(function(){
        $(this).addClass("now").siblings().removeClass("now");
    });
    $('#mainnav li').hover( //鼠标滑过导航栏目时
        function(){
            $(this).addClass("golist").siblings().removeClass("golist");
            $('.golist').addClass("open");
            $('.golist a').attr("aria-expanded",true);
            $('.golist ul').removeAttr("style");
        },
        function(){
            $('.golist').removeClass("open"); //鼠标移开后隐藏下拉列表
            $('.golist a').attr("aria-expanded",false);
            $('.golist ul').css("disply","none");
        }
    );
    $('.golist>ul').hover( //鼠标滑过下拉列表自身也要显示，防止无法点击下拉列表
        function(){
            ('.golist>ul').show();
        },
        function(){
            ('.golist>ul').hide();
        }
    );
    //导航栏固定
    $(window).scroll(function(){
        var top=$(window).scrollTop();
        if(top>=58){
            $("#expheadertop").addClass("fix");
            $("#expheadertop").css({color:"red",top:0});
        }else{
            $("#expheadertop").removeClass("fix");}
    });
    //service_one页面联系信息弹出
    $("#clickself").click(function(){
        $(".selfdesc").toggle();
    });
    //personal页面切换
    $(".left-thing>ul>li").click(function(){
        var i=$(this).index();
      $(this).addClass("liact").siblings().removeClass("liact");
        $(".thing-con>div").eq(i).show().siblings().hide();
    });
       //分页切换
    $(".pageshow li").click(function(){
        $(this).addClass("actnum").siblings().removeClass("actnum");
    });
});
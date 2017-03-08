/**
 * Created by thinkgamer on 17-3-9.
 */
$(document).ready(function() {
    $('#featured-area ul').roundabout({
        easing: 'easeOutInCirc',
        duration: 600,
        autoplay: true,
        autoplayDuration: 3000,
        autoplayPauseOnHover: true,
        minScale: 0.7,
        btnPrev: ".ban_r_btn", // 右按钮
        btnNext: ".ban_l_btn" // 左按钮
    });

    //粒子背景
    $('#particles').particleground({
        dotColor: '#9d9d9d',
        lineColor: '#999999'
    });
});
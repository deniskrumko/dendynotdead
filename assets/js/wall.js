function SetHeight(){
    var h = $(window).height();
    $("#scroll-content").height(h-160);    
}

$(document).ready(SetHeight);
$(window).resize(SetHeight);

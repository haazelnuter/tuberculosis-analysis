var mousepos={};
$(window).mousemove(function(e){
  mousepos.x=e.pageX;
  mousepos.y=e.pageY;
    //$(".cover").css("margin-left","calc(45% + "+mousepos.x/80+"px)");
});
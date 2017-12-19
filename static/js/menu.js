$(document).ready(function() {

  $("#toggle-menu").click(function() {
    $('.ui.sidebar').sidebar('setting', 'transition', 'overlay').sidebar('toggle');
  });

})

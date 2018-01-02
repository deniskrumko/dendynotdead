$(document).ready(function() {

  var $document = $(document),
    $element = $('#slim-menu'),
    className = 'hide-slim-menu'
  size = 150;

  if ($document.scrollTop() >= size) {
    $element.removeClass(className);
  } else {
    $element.addClass(className);
  }


  $document.scroll(function() {
    if ($document.scrollTop() >= size) {
      $element.removeClass(className);
    } else {
      $element.addClass(className);
    }
  });

  $(".toggle-menu").click(function() {
    $('.ui.sidebar').sidebar('setting', 'transition', 'overlay').sidebar('setting', 'mobileTransition', 'overlay').sidebar('toggle');
  });

})

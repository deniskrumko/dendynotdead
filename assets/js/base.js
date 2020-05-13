// Base Javascript for pages

$(document).ready(function(){
  // Dropdown for mobile menu
  $('.ui.dropdown').dropdown();

  $( "#change-lang" ).click(function() {
    $('.page').dimmer('show');
  });

})

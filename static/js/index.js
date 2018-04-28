$(document).ready(function() {
  $(".track").hover(function () {
    var name = $(this).data("name");
    $("#index-track-name").text(name);
  },
  function () {
    $("#index-track-name").text("Показать все треки");
  });
});

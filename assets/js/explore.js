$(document).ready(function(){
  $('.ui.accordion')
  .accordion()
;

 })


document.addEventListener('play', function(e) {
    var audios = document.getElementsByTagName('audio');
    for (var i = 0, len = audios.length; i < len; i++) {
        if (audios[i] != e.target) {
            audios[i].pause();
        }
    }
}, true);

var like_id = 0;
var number_prefix = 'number';

function incrementValue(clicked_id) {
    var value = parseInt(document.getElementById(clicked_id).innerHTML);
    value++;
    document.getElementById(clicked_id).textContent = value;
  }

function myFunction(clicked_id) {
    like_id = clicked_id
    number_id = number_prefix.concat(clicked_id);
    incrementValue(number_id);
    $('#explore_form').submit();
}



$(document).on('submit', '#explore_form', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/explore/',
        data: {
            like: like_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function() {

        }
    });
});

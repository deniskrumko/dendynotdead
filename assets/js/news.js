
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
    $('#news_form').submit();
}



$(document).on('submit', '#news_form', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/news/1/',
        data: {
            like: like_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function() {

        }
    });
});

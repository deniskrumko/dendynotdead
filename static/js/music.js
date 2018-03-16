$(function() {

  $('.ui.sticky')
    .sticky({
      context: '#example1',
      offset: 70,
      bottomOffset: 750,
    });

  // Setup the player to autoplay the next track
  var a = audiojs.createAll({
    trackEnded: function() {
      // Shitty way to search next available track
      var next = $('.track.playing').parent().parent().next().next().next().find('.track');

      // If there are no next track - then play first
      if (!next.length) next = $('.track').first();

      // Remove "Play corner" and "playing" class from currently playing track
      $('.track.playing').parent().prev().find('.corner').addClass('displaynone');
      $('.track.playing').removeClass('playing');

      // Add these attributes to next track
      next.addClass('playing');
      next.parent().prev().find('.corner').removeClass('displaynone');

      // Load music and play it!
      audio.load(next.attr('data-src'));
      audio.play();
    }
  });

  // Load in the first track
  var audio = a[0];
  first = $('.track').attr('data-src');
  $('.track').first().addClass('playing');
  audio.load(first);

  // Load in a track on TRACK NAME click
  $('.track').click(function(e) {
    e.preventDefault();

    if ($(this).hasClass('playing')) {
      if (audio.playing) {
        audio.pause();
      } else {
        audio.play();
      }
    } else {
      $('.track.playing').parent().prev().find('.corner').addClass('displaynone');
      $('.track.playing').removeClass('playing');

      $(this).addClass('playing');
      $(this).parent().prev().find('.corner').removeClass('displaynone');
      audio.load($(this).attr('data-src'));
      audio.play();
    }
  });

  // Load in a track on PLAY CORNER LABEL click
  $('.track-image').click(function(e) {
    var $track = $(this).next().find('.track');
    if ($track.hasClass('playing')) {
      if (audio.playing) {
        audio.pause();
      } else {
        audio.play();
      }
    } else {
      $('.track.playing').parent().prev().find('.corner').addClass('displaynone');
      $('.track.playing').removeClass('playing');

      $track.addClass('playing');
      $(this).find('a').removeClass('displaynone');
      audio.load($track.attr('data-src'));
      audio.play();
    }
  });
});

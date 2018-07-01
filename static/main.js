$().ready(function() {
  // will need to use event delegation
  $('.like').click(function(event) {
    let $icon = $(event.target);
    // $icon.toggleClass('unlike like');
    // $icon.toggleClass('far fas');
    let messageId = $icon.attr('data-messageid');
    $.ajax(`/message/${messageId}/like`).then(() => {
      alert('YOU LIKED IT');
      // $icon.text('Unlike');
    });
  });
  $('.unlike').click(function(event) {
    let $icon = $(event.target);
    // $icon.toggleClass('unlike like');
    // $icon.toggleClass('fas far');
    let messageId = $icon.attr('data-messageid');
    $.ajax(`/message/${messageId}/unlike`).then(() => {
      alert('YOU UNLIKED IT');
      // $icon.text('Like');
    });
  });
});

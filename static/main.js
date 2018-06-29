$().ready(function() {
  // will need to use event delegation
  $('.likebtn').click(function(event) {
    let $button = $(event.target);
    // $button.toggleClass('unlikebtn likebtn');
    let messageId = $button.attr('data-messageid');
    $.ajax(`/message/${messageId}/like`).then(() => {
      alert('YOU LIKED IT');
      $button.text('Unlike');
    });
  });
  $('.unlikebtn').click(function(event) {
    let $button = $(event.target);
    // $button.toggleClass('unlikebtn likebtn');
    let messageId = $button.attr('data-messageid');
    $.ajax(`/message/${messageId}/unlike`).then(() => {
      alert('YOU UNLIKED IT');
      $button.text('Like');
    });
  });
});

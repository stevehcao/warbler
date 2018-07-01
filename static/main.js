$().ready(function() {
  // will need to use event delegation
  $('.message-area').on('click', '.like', event => {
    let $icon = $(event.target);
    $icon.toggleClass('like unlike');
    $icon.toggleClass('far fas');
    let messageId = $icon.attr('data-messageid');
    let req = $.ajax(`/message/${messageId}/like`).then(() => {
      alert('YOU LIKED IT');
      // $icon.text('Unlike');
    });
  });

  // works for DB but not html
  // $('.like').click(function(event) {
  //   let $icon = $(event.target);
  //   // $icon.toggleClass('unlike like');
  //   // $icon.toggleClass('far fas');
  //   let messageId = $icon.attr('data-messageid');
  //   let req = $.ajax(`/message/${messageId}/like`).then(() => {
  //     alert('YOU LIKED IT');
  //     // $icon.text('Unlike');
  //   });
  // use .load?
  //$('.like').load('')
  // req.done(function(data) {
  //   // overwrite page
  //   $('.like').html(data)
  // })
  // });

  $('.message-area').on('click', '.unlike', event => {
    let $icon = $(event.target);
    $icon.toggleClass('unlike like');
    $icon.toggleClass('fas far');
    let messageId = $icon.attr('data-messageid');
    let req = $.ajax(`/message/${messageId}/unlike`).then(() => {
      alert('YOU UNLIKED IT');
    });
  });
  // works for db but not html
  // $('.unlike').click(function(event) {
  //   let $icon = $(event.target);
  //   // $icon.toggleClass('unlike like');
  //   // $icon.toggleClass('fas far');
  //   let messageId = $icon.attr('data-messageid');
  //   $.ajax(`/message/${messageId}/unlike`).then(() => {
  //     alert('YOU UNLIKED IT');
  //     // $icon.text('Like');
  //   });
  // });
});

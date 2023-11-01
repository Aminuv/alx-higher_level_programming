$(document).ready(function () {
    // Click event to the translate button.
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});

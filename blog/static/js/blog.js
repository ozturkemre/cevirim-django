$(document).ready(function(){
    $("#input").val("");
    $("#translated").val("");
  $("button").click(function(){
      var text = $("#input").val();
      var srce = document.getElementById("src");
      var src = srce.options[srce.selectedIndex].value;
      var deste = document.getElementById("dest");
      var dest = deste.options[deste.selectedIndex].value;
      $.ajax({
        url: '/ajax/translate_text/',
        data: {
          'text': text,
          'src': src,
          'dest': dest
        },
        dataType: 'json',
        success: function (data) {
          $('#translated').val(data.translated);

        }
      });
})
})
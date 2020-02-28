/*
  Modal Logic
 */
$('.close').on('click', function() {
  $('.modal').toggle();
});

$('#addHoursButton').on('click', function () {
  $.ajax({
            url: "track-hours-form",
    success: function(result){
    $('#addHoursModal').toggle();
  }});
});

/*
  Date Picker logic
 */

$('.datetime-input').datetimepicker({
    format:'YYYY-MM-DD'
});
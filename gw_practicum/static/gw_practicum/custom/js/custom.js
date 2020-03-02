/*
  Modal Logic
 */
$('.close').on('click', function() {
  $('.modal').hide();
});

$('#addHoursButton').on('click', function () {
    $('#addHoursModal').toggle();
});

$('.deleteHours').on('click', function() {
    hoursId = $(this).data('id');
    practicum = $(this).data('practicum');
    $('#removeHoursModal').toggle();
    $('#deleteHoursAffirm').on('click', function() {
        $.ajax({
            url: "/remove/" + practicum + '/' + hoursId,
            success: function(result){
            console.log(result)
                window.location.reload();
        }});
    });
});

/*
  Date Picker logic
 */

$('.datetime-input').datetimepicker({
    format:'YYYY-MM-DD'
});
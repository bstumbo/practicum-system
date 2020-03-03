/*
  Modal Logic
 */
$('.close').on('click', function() {
  $('.modal').hide();
  $('form#addHours').trigger('reset');
    if ($('input#hours_id').length) {
        $('input#hours_id').remove()
    }
});

// Add Hours
$('#addHoursButton').on('click', function () {
    $('#addHoursModal').toggle();
});

//Delete Hours
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

//Edit Hours
$('.editHours').on('click', function() {
    hoursId = $(this).data('id');
    $.ajax({
        url: "/edit-hours/" + hoursId,
        success: function(result){
            console.log(result)
            $('<input>', {
                type: 'hidden',
                id: 'hours_id',
                name: 'hours_id',
                value: hoursId
            }).appendTo('form#addHours');

            $('#id_start_date').val(result.hours.start_date);
            $('#id_end_date').val(result.hours.end_date);
            $('#id_hours').val(result.hours.hours);
            $('#id_tasks').val(result.hours.tasks);
            $('#hours_id').val(hoursId);
            $('#addHoursModal').toggle();
    }});
});

/*
  Date Picker logic
 */

$('.datetime-input').datetimepicker({
    format:'YYYY-MM-DD'
});
$(function () {
    $('#course option').hide()
    $('#department').on('change', function () {
        $('#course option').hide()
        var parent = $(this).val()
        $('#course option[data-parent=' + parent + ']').show()
    });

})
// WOW animation
new WOW().init();

$(document).ready(function() {
// Button submit loading
$('#btn-one').click(function() {
    $('#btn-one').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
});

// Button back
$('#back-btn').on('click', function(e){
    e.preventDefault();
    window.history.back();
});

//Reset form
$('form').each(function() {
    this.reset()
})

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $("#previewImage").attr('src', e.target.result);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

$("#inputGroupFile01").change(function(){
    readURL(this);
    $("#previewImage").css({visibility: "visible"})
});
});
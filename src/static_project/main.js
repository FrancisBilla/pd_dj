$(document).ready(function(){
  alert("OK");
    $('.ui.dropdown')
        .dropdown()

        $('.massage .close')
        .on('click', function(){
            $(this)
            .closest('.massage')
            .transition('fade')
            ;
    })
  ;

    $('#modal-btn').click(function(){
      $('.ui.modal')
       .modal('show')
      ;
    })

;
})
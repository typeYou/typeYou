(function($){
  $(function(){

// Initialize collapse button
$('.button-collapse').sideNav({
      edge: 'left',
    }
  );
// Initialize collapsible (uncomment the line below if you use the dropdown variation)
//$('.collapsible').collapsible();

$(document).ready(function(){
  // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
  $('.modal-trigger').leanModal();
});

$(document).ready(function() {
  $('input#input_text, textarea#textarea1').characterCounter();
});

//  $('.parallax').parallax();


  }); // end of document ready
})(jQuery); // end of jQuery name space

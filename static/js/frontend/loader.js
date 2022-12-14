$(document).ready(function(){
    setTimeout(()=> {
        $('.loader').remove();
    } , 2500); // after 2.5 sec it will remove.
    setTimeout(()=> {
        $('.left-div').addClass("active");
        $('.right-div').addClass("active");
        $('.left-div-mobile').addClass("active");
        $('.right-div-mobile').addClass("active");
    } , 2700); // after 2.5 sec it will remove.
});


$(window).scroll(function(){
    if ($(this).scrollTop() > 240) {
        $('.navbar').addClass('n_a_v')
    }
    else{
        $('.navbar').removeClass('n_a_v')
    }
  });


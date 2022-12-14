$(document).ready(function(){
    setTimeout(()=> {
        $('.loader').remove();
    } , 2500); // after 2.5 sec it will remove.
    setTimeout(()=> {
        $('.left-div').addClass("active");
        $('.right-div').addClass("active");
    } , 2700); // after 2.5 sec it will remove.
});





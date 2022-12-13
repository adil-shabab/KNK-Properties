jQuery("#id_buy_rent option").each(function(i, e) {
    (jQuery("<input type='radio' name='r' />")
      .attr("value", jQuery(this).val())
      .attr("checked", i == 0)
      .click(function() {
        jQuery("#id_buy_rent").val(jQuery(this).val());
      }).add($("<label>"+ this.textContent +"</label>")))
      .appendTo("#r");
  });
  

const text = '---------';
let matches = []

for (const div of document.getElementById('r').getElementsByTagName('label')) {
  if (div.textContent.includes(text)) {
    div.innerHTML = 'All'
  }
}


for (const div of document.getElementById('id_property_type').getElementsByTagName('option')) {
  if (div.textContent.includes(text)) {
    div.innerHTML = 'All'
  }
}


// modal 
document.getElementById('price_modal_body').querySelectorAll('input').forEach((input)=>input.addEventListener('input', function(){
    let min_value = document.getElementById('id_min_price').value
    let max_value = document.getElementById('id_max_price').value
    document.getElementById('price_modal_btn').innerHTML = min_value + ' - ' + max_value + ' AED '
}))




// modal 
document.getElementById('bed_modal_body').querySelectorAll('input').forEach((input)=>input.addEventListener('input', function(){
    let min_bed = document.getElementById('id_min_count_bedroom').value
    let max_bed = document.getElementById('id_max_count_bedroom').value
    let min_bath = document.getElementById('id_min_count_bathroom').value
    let max_bath = document.getElementById('id_max_count_bathroom').value
    if (max_bed != "" & max_bath !=0 ){
        document.getElementById('bed_modal_btn').innerHTML = min_bed + " - " + max_bed + " | " + min_bath + " - " + max_bath
    }else{
        document.getElementById('bed_modal_btn').innerHTML = "Bed | Bath"
    }
}))





// modal 
document.getElementById('area_modal_body').querySelectorAll('input').forEach((input)=>input.addEventListener('input', function(){
    let min_area = document.getElementById('id_min_count_area').value
    let max_area = document.getElementById('id_max_count_area').value
    if (max_area != "" ){
        document.getElementById('area_modal_btn').innerHTML = min_area + " - " + max_area
    }else{
        document.getElementById('area_modal_btn').innerHTML = "Area"
    }
}))







// owl carousel in property bbox 
$('.img-box').owlCarousel({
  loop:true,
  margin:10,
  nav:false,
  items:1,
  autoplay:true,
  autoplayTimeout:5000,
})





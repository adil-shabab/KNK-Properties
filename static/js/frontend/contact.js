

$("#phone").intlTelInput({
    initialCountry: "AE",
    separateDialCode: true,
});

document.querySelector('#contact-form').addEventListener('submit',function(e){

    e.preventDefault()
    txt = document.querySelector('.iti__selected-dial-code').innerHTML


    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let message = document.getElementById('message').value
    let number = txt + document.getElementById('phone').value

    console.log(number)
    var csrftoken = document.getElementById('csrf_token').innerText
    fetch('http://139.59.32.134/account/create/message', {
    method: 'POST',
    headers:{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
        'number': number,
        'name': name,
        'email': email,
        'message': message,

    })
    })
    .then(res => {
    return res.json()
    })
    .then(data => popup())
    .catch(error => console.log(error))


})



function popup(){
    document.getElementById('name').value = ""
    document.getElementById('email').value = ""
    document.getElementById('message').value = ""
    document.getElementById('phone').value = ""
    swal(
        'Success',
        'Your Message has been Sent',
        'success'
    )
}



$('.counter').countUp(
    {
    delay: 5,
    time: 1500
    }
);

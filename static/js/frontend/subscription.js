

document.querySelector('#subscription__form').addEventListener('submit',function(e){
    e.preventDefault()
     
    let email = document.getElementById('subscription__email').value
    var csrftoken = document.getElementById('csrf_token').innerText
    fetch('http://139.59.32.134/account/create/subscription', {
    method: 'POST',
    headers:{
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
        'email': email,
    })
    })
    .then(res => {
    return res.json()
    })
    .then(data => console.log(data))
    .then(data => popup())
    .catch(error => console.log(error))
})



function popup(){
    document.getElementById('subscription__email').value = ""
    swal(
        'Success',
        'Your Subscription Added',
        'success'
    )
}
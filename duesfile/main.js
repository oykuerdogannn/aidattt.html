const counters = document.querySelectorAll('.number');

counters.forEach(counter => {
  const updateCount = () => {
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;

    const increment = target / 200;

    if(count < target){
      counter.innerText = Math.ceil(count + increment);
      setTimeout(updateCount, 10); 
    } else {
      counter.innerText = target.toLocaleString(); 
    }
  }

  updateCount();
});

function openLogin(){
document.getElementById("loginBox").style.display="block"
}

function closeLogin(){
document.getElementById("loginBox").style.display="none"
}

function login(){

let user = document.getElementById("username").value
let pass = document.getElementById("password").value
let msg = document.getElementById("loginMessage")

if(user === "admin" && pass === "1234"){

msg.style.color="green"
msg.innerText="Giriş başarılı"

setTimeout(()=>{
closeLogin()
},1000)

}else{

msg.style.color="red"
msg.innerText="Kullanıcı adı veya şifre yanlış"

}

}
function ekle(){

let ad = document.getElementById("ad").value
let aidat = document.getElementById("aidat").value

if(ad=="" || aidat==""){
alert("Bilgileri doldurun")
return
}

kisiler.push({
ad:ad,
aidat:aidat,
odendi:false
})

goster()

}

function goster(){

let tablo=""

kisiler.forEach((k,i)=>{

tablo+=`
<tr>
<td>${k.ad}</td>
<td>${k.aidat} ₺</td>
<td class="${k.odendi ? 'odendi':'odenmedi'}">
${k.odendi ? 'Ödendi':'Ödenmedi'}
</td>

<td>
<button onclick="ode(${i})">Ödendi Yap</button>
<button onclick="sil(${i})">Sil</button>
</td>
</tr>
`

})

document.getElementById("liste").innerHTML=tablo

}

function ode(i){
kisiler[i].odendi=true
goster()
}

function sil(i){
kisiler.splice(i,1)
goster()
}


let kisiler = []

try {

let data = localStorage.getItem("kisiler")

if(data){
kisiler = JSON.parse(data)
}

} catch(e) {

console.log("JSON okuma hatası", e)
kisiler = []

}

function ekle(){

let ad = document.getElementById("ad").value
let aidat = document.getElementById("aidat").value

if(ad=="" || aidat==""){
alert("Bilgileri doldurun")
return
}

kisiler.push({
ad:ad,
aidat:aidat,
odendi:false
})

kaydet()
goster()

}

function goster(){

let tablo=""

kisiler.forEach((k,i)=>{

// Destructuring
const {ad, aidat, odendi} = k

tablo+=`
<tr>
<td>${ad}</td>
<td>${aidat} ₺</td>

<td class="${odendi ? 'odendi':'odenmedi'}">
${odendi ? 'Ödendi':'Ödenmedi'}
</td>

<td>
<button onclick="ode(${i})">Ödendi Yap</button>
<button onclick="sil(${i})">Sil</button>
</td>
</tr>
`

})

document.getElementById("liste").innerHTML=tablo

}

function ode(i){
kisiler[i].odendi = true
kaydet()
goster()
}

function sil(i){
kisiler.splice(i,1)
kaydet()
goster()
}

// JSON + LocalStorage
function kaydet(){
localStorage.setItem("kisiler", JSON.stringify(kisiler))
}


// ------------------
// Fetch API + Async
// ------------------

async function veriGetir(){

try{

let response = await fetch("https://jsonplaceholder.typicode.com/users")

let data = await response.json()

console.log("Fetch API örnek veri:", data)

}catch(error){

console.log("Hata oluştu",error)

}

}

veriGetir()


// ------------------
// Promise Örneği
// ------------------

function promiseOrnek(){

return new Promise((resolve,reject)=>{

setTimeout(()=>{

resolve("Promise çalıştı")

},1000)

})

}

promiseOrnek().then(sonuc=>{
console.log(sonuc)
})


// Sayfa açılınca tabloyu göster
goster()



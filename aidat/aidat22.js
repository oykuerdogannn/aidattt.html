class Apartment{
    constructor(name, amount) {
        this.name = name;
        this.amount = amount;

    }
}

let apartments = [];

document.getElementById("add").addEventListener("click", addApartment);
document.getElementById("calculate").addEventListener("click", calculate);

function addApartment() {

    let name = document.getElementById("apartmentName").value.trim();
    let amount = document.getElementById("apartment expense").value;

    if (name === "" || amount === "") {
        alert("Lütfen tüm alanlari doldurun");
        return;
    }

    name = name.toUpperCase();

    let apartment = new Apartment(name, Number(amount));

    apartments.push(apartment);

    document.getElementById("apartmentName").value = "";
    document.getElementById("apartment expense").value = "";

    showList();
    saveData();
}

function showList() {

    let output = "";

    for (let { name, amount } of apartments) {
        output += `${name} - ${amount} TL<br>`;
    }

    document.getElementById("list").innerHTML = output;
}

function calculate() {

    let total = apartments.reduce((sum, apt) => sum + apt.amount, 0);

    if (apartments.length === 0) {
        document.getElementById("conclusion").innerHTML = "No apartment added!";
    } else {

        let average = total / apartments.length;

        document.getElementById("conclusion").innerHTML =
            "Toplam Gider: " + total.toFixed(2) + " TL <br>" +
            "Daire Basina Ücret: " + average.toFixed(2) + " TL";
    }
}

const totalCalculate = () => {
    return apartments.reduce((sum, apt) => sum + apt.amount, 0);
};

const saveData = () => {
    localStorage.setItem("apartments", JSON.stringify(apartments));
};

const loadData = () => {
    let data = localStorage.getItem("apartments");
    if (data) {
        let parsed = JSON.parse(data);
        apartments = parsed.map(a => new Apartment(a.name, a.amount));
        showList();
    }
};

window.onload = loadData;

const getPromiseData = () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data Ready");
        }, 1000);
    });
};

const runAsync = async () => {
    let result = await getPromiseData();
    console.log(result);
};

runAsync();

const fetchUsers = async () => {
    try {
        let response = await fetch("https://jsonplaceholder.typicode.com/users");
        let data = await response.json();
        console.log("Users from API:", data);
    } catch (error) {
        console.log("Error:", error);
    }
};

fetchUsers();
// Haetaan ja alustetaan HTML-sivun elementtejä omiin muuttujiinsa id:n perusteella
const number1El = document.getElementById("number1");
const number2El = document.getElementById("number2");
const operatorEl = document.getElementById("operator");
const answerEl = document.getElementById("answer");
const submitButton = document.getElementById("submit");
const taskNumberEl = document.getElementById("task-number");
const resultEl = document.getElementById("result");
const finalScoreEl = document.getElementById("final-score");

// Tehtävän numero ja pisteet muuttujissa
let currentTask = 1;
let points = 0;

// Luo uuden laskutehtävän satunnaisilla luvuilla
function newQuestion() {
    const number1 = Math.floor(Math.random() * 10) + 1; // Satunnainen luku välillä 1–10
    const number2 = Math.floor(Math.random() * 10) + 1; // Toinen satunnainen luku välillä 1–10

    number1El.textContent = number1; // Näytetään ensimmäinen luku HTML:ssä
    number2El.textContent = number2; // Näytetään toinen luku HTML:ssä
}

// Tarkistaa käyttäjän vastauksen ja lisää pisteen, jos vastaus on oikea
function answerCheck() {
    const number1 = parseInt(number1El.textContent); // Haetaan ensimmäinen luku ja parsitaan se integeriksi
    const number2 = parseInt(number2El.textContent); // Haetaan toinen luku ja parsitaan se integeriksi

    const answer = parseInt(answerEl.value); // Haetaan käyttäjän syöttämä vastaus ja parsitaan sekin integeriksi

    if (answer == number1 + number2) { // Tarkistetaan yksinkertaisesti onko vastaus sama kuin arvottujen lukujan yhteenlaskun tulos
        points++; // Lisätään piste
    }
}

// Päivittää pelin tilanteen seuraavaan tehtävään tai päättää pelin
function gameUpdate() {
    if (currentTask < 5) { // Jos tehtäviä on alle 5
        currentTask++; // Siirrytään seuraavaan tehtävään
        taskNumberEl.textContent = currentTask; // Päivitetään tehtävän numero HTML:ssä
        newQuestion(); // Luodaan uusi tehtävä newQuestion()-funktiota kutsumalla
        answerEl.value = ""; // Tyhjennetään vastauskenttä
    } else { 
        endGame(); // Peli päättyy, jos tehtäviä on ollut 5
    }
}

// Päättää pelin ja näyttää lopputuloksen
function endGame() {
    resultEl.style.display = "block"; // Näytetään tulosteksti, joka oli aiemmin piilossa
    finalScoreEl.textContent = points; // Näytetään pelaajan pisteet
    document.getElementById("question").style.display = "none"; // Piilotetaan osiot, joita ei haluta näyttää
    document.getElementById("submit").style.display = "none"; 
    document.getElementById("task-info").style.display = "none"; 
    document.getElementById("answer-section").style.display = "none"; 
}

// initGame() alustaa pelin ja lisää tapahtumankäsittelijän lähetysnapille
function initGame() {
    newQuestion(); // Luodaan ensimmäinen tehtävä
    submitButton.addEventListener("click", () => { 
        answerCheck(); // Tarkistetaan vastaus, kun submitButton on painettu
        gameUpdate(); // Päivitetään peli seuraavaan tehtävään
    });
}

// Käynnistetään peli kutsumalla initGame() -funktiota
initGame();

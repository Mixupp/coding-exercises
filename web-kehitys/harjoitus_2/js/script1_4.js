// Määritetään valuuttakurssit HTML-objektiin

const exchangeRates = {
    EUR: { USD: 1 / 0.9, GBP: 1 / 1.2},
    USD: { EUR: 0.9, GBP: 0.9 / 1.2 },
    GBP: { EUR: 1.2, USD: 1.2 / 0.9 }
}
/* Funktio valuutan muuntamiselle, parametreinä muunnettava summa, valuutta josta muunnetaan ja
    valuutta, joksi muunnetaan */
function currencyConversion(amount, inCurrency, toCurrency) {

    // Jos muunnettava valuutta on sama, niin valuutan arvo pysyy samana
    if (inCurrency == toCurrency) {
        return amount;
    }
    /* amount eli muunnettava summa valuuttaa kerrotaan muuntosuhteella, joka saadaan oliosta exchangeRates.
        Ensin haetaan valuutta, josta muunnetaan indeksillä inCurrency, sitten siirrytään kerrosta alemmas ja haetaan
        valuutta johon muunnetaan indeksistä toCurrency
        */
    return amount * exchangeRates[inCurrency][toCurrency]
}

// Haetaan syöte-elementit muuttujiin.
const inputAmount = document.getElementById("inputAmount");
const outputAmount = document.getElementById("outputAmount");
const inputCurrency = document.getElementById("inputCurrency");
const outputCurrency = document.getElementById("outputCurrency");


/* Luodaan event listenerit syötekentille sekä valintakentille. Jos tapahtuu muutos
    jossakin kentässä tai valinnassa, kutsutaan updateValues() -funktiota, joko argumentilla true tai false.
*/

inputAmount.addEventListener("input", () => updateValues(true));
inputCurrency.addEventListener("change", () => updateValues(true));
outputAmount.addEventListener("input", () => updateValues(false));
outputCurrency.addEventListener("change", () => updateValues(false));

/*  Funktio arvojen päivittämiselle muutoksen tapahduttua jossakin kentässä.
    Kun parametri input saa arvoksi "true" ylemmän syöttökentän arvo luetaan muuttujaan amount.
    inCurrency saa valuutan arvon, josta halutaan muuntaa ja toCurrency sen valuutan arvon, johon muunnetaan.
    Lopuksi outputAmount -kenttään palautetaan currencyConversion() -funktion palauttama arvo eli paljonko ylemmän kentän
    valuutta ja syötetty arvo on alemman kentän valuuttana.
    Jos saadaan argumenttina "false", eli muutos tapahtuu alemmissa kentissä toimitaan päinvastoin ja 
    arvo lasketaan ylempään input-kenttään.
    */
function updateValues(input) {
    if (input) {
        const amount = parseFloat(inputAmount.value);
        const inCurrency = inputCurrency.value;
        const toCurrency = outputCurrency.value;
        outputAmount.value = currencyConversion(amount, inCurrency, toCurrency).toFixed(2);
    }
    else {
        const amount = parseFloat(outputAmount.value);
        const inCurrency = outputCurrency.value;
        const toCurrency = inputCurrency.value;
        inputAmount.value = currencyConversion(amount, inCurrency, toCurrency).toFixed(2);
    }

}


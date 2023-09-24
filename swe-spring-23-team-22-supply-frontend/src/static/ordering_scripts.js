// Calculate price of vaccines to be ordered
function calcPrice() {
    var vaccPrices = {
        "- Select -": 0,
        "Anthrax": 900,
        "Cholera": 1.7,
        "Covid-19": 90,
        "Hepatitis A": 67.68,
        "Hepatitis B": 32.43,
        "Human Papillomavirus (HPV)": 164.56,
        "Measles": 55.89,
        "Mumps": 55.89,
        "Polio": 0.14,
        "Rabies": 1700,
        "Seasonal Influenza (Flu)": 13.41,
        "Shingles": 360,
        "Smallpox": 7.46,
        "Tetanus": 17.28,
        "Tuberculosis": 85.39,
        "Typhoid Fever": 127.54,
    }

    var vaccForm = document.getElementById("vaccine-type")
    var vaccType = vaccForm.options[vaccForm.selectedIndex].text
    var vaccPrice = vaccPrices[vaccType]
    var quantity = document.getElementById("quantity").value

    var total_price = document.getElementById("total-price")
    total_price.innerHTML = "$" + (vaccPrice * quantity).toFixed(2) 

}
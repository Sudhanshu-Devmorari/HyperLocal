// // Define the city data object
// var myArray = {
//     "Alaska": ['a', 'b', 'c'],
//     "Arizona": ['d', 'e', 'f'],
//     "Arkansas": ['x', 'y', 'z']
//   };

// // Get the select element and city display element
// var stateSelect = document.getElementById("stateSelect");
// var cityDisplay = document.getElementById("cityDisplay");

// // Function to handle state change
// function handleStateChange() {
// var selectedState = stateSelect.value;
// var cities = myArray[selectedState];
// cityDisplay.textContent = JSON.stringify(cities);
// console.log(cities)
// }

// // Add event listener for state select click
// stateSelect.addEventListener("click", handleStateChange);

// // Add event listener for state select change
// stateSelect.addEventListener("change", handleStateChange);

function send_data() {
    var value = document.getElementById("id_state").value;
    // console.log(value);

    var data = {
        "AL": ['Birmingham', 'Huntsville', 'Mobile'],
        "AK": ['Anchorage', 'Fairbanks',],
        "AZ": ['Phoenix', 'Prescott', 'Scottsdale','Tuscon'],
        "AR": ['Little Rock'],
        "CA": ["Bakersfield", "Fresno", "Long Beach", "Los Angeles", "Napa",
                    "Oakland", "Orange County", "Riverside", "Sacramento", "San Diego",
                    "San Francisco", "San Jose", "San Luis Obispo", "Santa Barbara", "Santa Cruz"
                    ],
        "CO": ['Colorado Springs', 'Denver', 'Grand Junction', 'Pueblo'],
        "CT": ['Bridgeport', 'Hartford', 'New Haven'],
        "DE": ['Wilmington'],
        "FL": ['Daytona Beach', 'Fort Lauderdale', 'Jacksonville', 'Key West', 'Miami', 'Orlando', 'Tampa', 'West Palm Beach'],
        "GA": ['Atlanta', 'Columbus', 'Savannah'],
        "HI": ['Honolulu'],
        "ID": ['Boise City'],
        "IL": ['Bloomington', 'Champaign', 'Chicago'],
        "IN": ["Indianapolis", "Muncie", "South Bend"],
        "IA": ['Des Moines','Cedar Rapids'],
        "KS": ['Wichita'],
        "KY": ['Lexington','Louisville'],
        "LA": ["Baton Rouge", "Lafayette", "New Orleans", "Shreveport"],
        "ME": ['Portland'],
        "MD": ['Baltimore'],
        "MA": ['Boston','Worcester'],
        "MI": ["Detroit", "Flint", "Grand Rapids"],
        "MN": ['Duluth','Minneapolis'],
        "MS": ['Jackson'],
        "MO": ["Kansas City", "St. Louis", "Springfield"],
        "MT": ['Billings'],
        "NE": ['Lincoln','Omaha'],
        "NV": ['Las Vegas','Reno'],
        "NH": ['Manchester'],
        "NJ": ['Atlantic City','Newark'],
        "NM": ['Albuquerue','Santa Fe'],
        "NY": ['Albany', 'Bronx', 'Brooklyn', 'Buffalo', 'Manhattan', 'New York City', 'Queens', 'Rochester', 'Staten Island'],
        "NC": ["Charlotte", "Durham", "Fayetteville", "Greensboro", "Raleigh"],
        "ND": ['Fargo'],
        "OH": ["Cincinnati", "Cleveland", "Columbus", "Dayton", "Toledo"],
        "Ok": ['Oklahoma City','Tulsa'],
        "OR": ['Portland'],
        "PA": ['Harrisburg', 'Philadelphia', 'Pittsburgh'],
        "RI": ['Providence'],
        "SC": ['Charleston','Columbia'],
        "SD": ['Sioux Falls'],
        "TN": ["Chattanooga", "Knoxville", "Nashville", "Memphis"],
        "TX": ["Austin", "Dallas", "El Paso", "Houston", "McAllen", "San Antonio", "Waco"],
        "UT": ['Salt Lake City'],
        "VT": ['Burlington'],
        "VA": ['Richmond','Virginia Beach'],
        "WA": ["Seattle", "Spokane", "Tacoma"],
        "WV": ['Charleston'],
        "WI": ["Green Bay", "Madison", "Milwaukee"],
        "WY": ['Cheyenne'],
        };

    var cities = data[value];
    // console.log(cities)
    const citySelect = document.getElementById('citySelect')
    // console.log(citySelect)
    while (citySelect.options.length > 0) {                
        citySelect.remove(0);
    }
    const selectEle = document.createElement('option')
    selectEle.textContent = "Select City"
    selectEle.disabled = true
    selectEle.selected = true
    citySelect.append(selectEle)
    for(var city of cities){
        const cityEle = document.createElement('option')
        cityEle.textContent = city
        cityEle.value = city
        citySelect.append(cityEle)
    }
}
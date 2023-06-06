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
    console.log(value);

    var data = {
        "Alabama": ['Birmingham', 'Huntsville', 'Mobile'],
        "Alaska": ['Anchorage', 'Fairbanks',],
        "Arizona": ['Phoenix', 'Prescott', 'Scottsdale','Tuscon'],
        "Arkansas": ['Little Rock'],
        "California": ["Bakersfield", "Fresno", "Long Beach", "Los Angeles", "Napa",
                    "Oakland", "Orange County", "Riverside", "Sacramento", "San Diego",
                    "San Francisco", "San Jose", "San Luis Obispo", "Santa Barbara", "Santa Cruz"
                    ],
        "Colorado": ['Colorado Springs', 'Denver', 'Grand Junction', 'Pueblo'],
        "Connecticut": ['Bridgeport', 'Hartford', 'New Haven'],
        "Deleware": ['Wilmington'],
        "Florida": ['Daytona Beach', 'Fort Lauderdale', 'Jacksonville', 'Key West', 'Miami', 'Orlando', 'Tampa', 'West Palm Beach'],
        "Georgia": ['Atlanta', 'Columbus', 'Savannah'],
        "Hawaii": ['Honolulu'],
        "Idaho": ['Boise City'],
        "Illinois": ['Bloomington', 'Champaign', 'Chicago'],
        "Indiana": ["Indianapolis", "Muncie", "South Bend"],
        "Iowa": ['Des Moines','Cedar Rapids'],
        "Kansas": ['Wichita'],
        "Kentucky": ['Lexington','Louisville'],
        "Louisiana": ["Baton Rouge", "Lafayette", "New Orleans", "Shreveport"],
        "Maine": ['Portland'],
        "Maryland": ['Baltimore'],
        "Massachusetts": ['Boston','Worcester'],
        "Michigan": ["Detroit", "Flint", "Grand Rapids"],
        "Minnesota": ['Duluth','Minneapolis'],
        "Mississippi": ['Jackson'],
        "Missouri": ["Kansas City", "St. Louis", "Springfield"],
        "Montana": ['Billings'],
        "Nebraska": ['Lincoln','Omaha'],
        "Nevada": ['Las Vegas','Reno'],
        "New Hampshire": ['Manchester'],
        "New Jersey": ['Atlantic City','Newark'],
        "New Mexico": ['Albuquerue','Santa Fe'],
        "New York": ['Albany', 'Bronx', 'Brooklyn', 'Buffalo', 'Manhattan', 'New York City', 'Queens', 'Rochester', 'Staten Island'],
        "North Carolina": ["Charlotte", "Durham", "Fayetteville", "Greensboro", "Raleigh"],
        "North Dakota": ['Fargo'],
        "Ohio": ["Cincinnati", "Cleveland", "Columbus", "Dayton", "Toledo"],
        "Oklahoma": ['Oklahoma City','Tulsa'],
        "Oregon": ['Portland'],
        "Pennsylvania": ['Harrisburg', 'Philadelphia', 'Pittsburgh'],
        "Rhode Island": ['Providence'],
        "South Carolina": ['Charleston','Columbia'],
        "South Dakota": ['Sioux Falls'],
        "Tennessee": ["Chattanooga", "Knoxville", "Nashville", "Memphis"],
        "Texas": ["Austin", "Dallas", "El Paso", "Houston", "McAllen", "San Antonio", "Waco"],
        "Utah": ['Salt Lake City'],
        "Vermont": ['Burlington'],
        "Virginia": ['Richmond','Virginia Beach'],
        "Washington": ["Seattle", "Spokane", "Tacoma"],
        "West Virginia": ['Charleston'],
        "Wisconsin": ["Green Bay", "Madison", "Milwaukee"],
        "Wyoming": ['Cheyenne'],
        };

    var cities = data[value];
    console.log(cities)
    const citySelect = document.getElementById('citySelect')
    console.log(citySelect)
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
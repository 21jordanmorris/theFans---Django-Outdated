var gameCard = document.getElementsByClassName("game-card");
var container = document.getElementsByClassName("container");
var current_date = "None";
var h4;

// CHANGE IN THE FUTURE
var july30 = [], july31 = [], aug1 = [], aug2 = [], aug3 = [], aug4 = [], aug5 = [],
    aug6 = [], aug7 = [], aug8 = [], aug9 = [], aug10 = [], aug11 = [], aug12 = [], aug13 = [], aug14 = [];

for (var i = 0; i < gameCard.length; i++)
{
    // Absolutely terrible waying of doing things but cannot think of a better solution at the 
    // moment to add headers while keeping flexbox. COME BACK AND CHANGE LATER
    var date = gameCard[i].getElementsByClassName("date").item(0).innerHTML;
    if (date == "July 30, 2020")
        july30.push(gameCard[i]);
    else if (date == "July 31, 2020")
        july31.push(gameCard[i]);
    else if (date == "Aug. 1, 2020")
        aug1.push(gameCard[i]);
    else if (date == "Aug. 2, 2020")
        aug2.push(gameCard[i]);
    else if (date == "Aug. 3, 2020")
        aug3.push(gameCard[i]);
    else if (date == "Aug. 4, 2020")
        aug4.push(gameCard[i]);  
    else if (date == "Aug. 5, 2020")
        aug5.push(gameCard[i]);
    else if (date == "Aug. 6, 2020")
        aug6.push(gameCard[i]);
    else if (date == "Aug. 7, 2020")
        aug7.push(gameCard[i]);
    else if (date == "Aug. 8, 2020")
        aug8.push(gameCard[i]);   
    else if (date == "Aug. 9, 2020")
        aug9.push(gameCard[i]);
    else if (date == "Aug. 10, 2020")
        aug10.push(gameCard[i]);
    else if (date == "Aug. 11, 2020")
        aug11.push(gameCard[i]);
    else if (date == "Aug. 12, 2020")
        aug12.push(gameCard[i]); 
    else if (date == "Aug. 13, 2020")
        aug13.push(gameCard[i]);
    else if (date == "Aug. 14, 2020")
        aug14.push(gameCard[i]);             
}

var days = [july30, july31, aug1, aug2, aug3, aug4, aug5, aug6, aug7, aug8, aug9, aug10, aug11, aug12, aug13, aug14]
var dayContainer, date, cardContainer

for (var i = 0; i < days.length; i++)
{
    dayContainer = document.createElement('div');
    date = document.createElement('h4');
    date.className = "date-header";
    date.textContent = days[i][0].getElementsByClassName("date").item(0).innerHTML;

    dayContainer.appendChild(date);

    cardContainer = document.createElement('div');
    cardContainer.className = "container";

    for (var j = 0; j < days[i].length; j++)
    {
        cardContainer.appendChild(days[i][j]);
    }

    dayContainer.appendChild(cardContainer);
    document.body.appendChild(dayContainer);
}
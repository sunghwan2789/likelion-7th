const weather = document.querySelector(".js-weather");
const API_KEY = "dd4921796c965b0ccbba3efc67e8b7f7";
const COORDS = "coords";

const getWeather = (lat, lng) => {
  fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
  )
    .then(response => response.json())
    .then(json => {
      const temperature = Math.floor(json.main.temp),
        description = json.weather[0].description

        weather.innerHTML = `${temperature}°C`;
      displayIcon(description);
      console.log(temperature, description);
    });
};

const displayIcon = (description) =>{
    const i = document.createElement("i");
    const icon = weather.appendChild(i);
    if(description === 'clear sky'){
        icon.className = "fas fa-sun"        
    }else if(description === 'haze' || 'few clouds' || 'scattered clouds'|| 'broken clouds'){
        icon.className = "fas fa-cloud";
    }else if(description ==='shower rain' || 'rain'){
        icon.className = "fas fa-cloud-showers-heavy"
    }else if(description ==='thunderstorm'){
        icon.className = "fas fa-bolt"
    }else if(description === 'snow'){
        icon.className = "far fa-snowflake"
    }else {
        icon.className ="far fa-times-circle"
    }
    
}

const saveCoords = coordsObj => {
  localStorage.setItem("coords", JSON.stringify(coordsObj));
};

const handleGeoSuccess = position => {
  console.log(position);
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  const coordsObj = {
    latitude,
    longitude
  };
  saveCoords(coordsObj);
  getWeather(latitude, longitude);
};

const handelGeoFailed = error => {
  console.log(error.message);
};

const askForCoords = () => {
  navigator.geolocation.getCurrentPosition(handleGeoSuccess, handelGeoFailed);
};

const loadCoords = () => {
  const loadedCoords = localStorage.getItem(COORDS);
  if (loadedCoords === null) {
    askForCoords();
  } else {
    const parseCoords = JSON.parse(loadedCoords);
    console.log(parseCoords.latitude, parseCoords.longitude);
    getWeather(parseCoords.latitude, parseCoords.longitude);
    
  }
};

function init() {
  loadCoords();
}

init();
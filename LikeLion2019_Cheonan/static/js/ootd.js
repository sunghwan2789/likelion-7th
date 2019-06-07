
        // 주소-좌표 변환 객체를 생성합니다
        var geocoder = new daum.maps.services.Geocoder();
        
const API_KEY = "dd4921796c965b0ccbba3efc67e8b7f7";
const COORDS = "coords";
const getWeather = async (lat, lng) => {
  return await fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
  )
    .then(response => response.json())
    .then(json => {
      return {
          temperature: Math.floor(json.main.temp),
          description: json.weather[0].description,
      }
    });
};
        
navigator.geolocation.getCurrentPosition(async function (pos) {
    let {latitude, longitude} = pos.coords;

    $('#position').text(`latitude: ${latitude} longitude: ${longitude}`)

    geocoder.coord2RegionCode(longitude, latitude, function (res) {
        $('[name=region]').val(res[0].address_name);
    });

    let {temperature, description} = await getWeather(latitude, longitude);
    $('[name=temperature]').val(temperature);
    let weather;
    switch (description) {
        case 'clear sky':
            weather = '맑음';
            break;
        case 'haze':
        case 'mist':
        case 'few clouds':
        case 'scattered clouds':
        case 'broken clouds':
            weather = '흐림';
            break;
        case 'shower rain':
        case 'rain':
        case 'thunderstorm':
            weather = '비';
            break;
        case 'snow':
            weather = '눈';
            break;
    }
    $('[name=weather]').val(weather);

});
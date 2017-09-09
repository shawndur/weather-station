function loadWeatherTable(){
  var ajaxRequest;

  try {
    ajaxRequest = new XMLHttpRequest();
  }catch (e) {
    try {
      ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
    }catch (e) {
      try{
        ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
      }catch (e){
        alert("Could not create ajax request");
        return false;
      }
    }
  }

  ajaxRequest.onreadystatechange = function(){
    if(ajaxRequest.readyState == 4){
      var ajaxDisplay = document.getElementById('weather-table');
      ajaxDisplay.innerHTML = ajaxRequest.responseText;
    }
  }

  /*

  var age = document.getElementById('age').value;
  var wpm = document.getElementById('wpm').value;
  var sex = document.getElementById('sex').value;
  var queryString = "?age=" + age ;

  queryString +=  "&wpm=" + wpm + "&sex=" + sex;
  */
  ajaxRequest.open("GET", "ajax-weather.php", true);
  ajaxRequest.send(null);
}

loadWeatherTable();

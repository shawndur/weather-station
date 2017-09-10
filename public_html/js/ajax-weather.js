var sortOrder = {
  asc: true,
  column: 'timestamp'
}

function loadWeatherTable() {
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

  var args = "?order=" + sortOrder.column + "&asc=" + sortOrder.asc;

  ajaxRequest.open("GET", "ajax-weather.php" + args, true);
  ajaxRequest.send(null);
}

function sortWeatherTable(column) {
  if (column == sortOrder.column) {
    sortOrder.asc = !sortOrder.asc;
  }
  sortOrder.column = column;

  loadWeatherTable();
}

loadWeatherTable();

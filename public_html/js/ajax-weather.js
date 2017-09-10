var sortOrder = {
  columnNames: ['time', 'temp', 'humidity', 'pressure'],
  asc: true,
  column: 0,
  columnName: function () {return this.columnNames[this.column]},
  sortOn: function (column) {
    if (this.column == column) {
      this.asc = !this.asc;
    }else{
      this.column = column;
    }
  }
}

var timeHeader = document.getElementById('th-time');
var tempHeader = document.getElementById('th-temp');
var humHeader = document.getElementById('th-hum');
var pressHeader = document.getElementById('th-press');

var curHeader = timeHeader;

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

  var args = "?order=" + sortOrder.columnName() + "&asc=" + sortOrder.asc;

  ajaxRequest.open("GET", "ajax-weather.php" + args, true);
  ajaxRequest.send(null);
}

function renderCaret(element, asc) {
  if (asc) {
    element.setAttribute('class', 'fa fa-caret-up');
  }else{
    element.setAttribute('class', 'fa fa-caret-down');
  }
}

function removeCaret(element) {
  element.setAttribute('class','');
}

function sortWeatherTable(column, element) {
  sortOrder.sortOn(column);
  removeCaret(curHeader);
  curHeader = element;
  renderCaret(element, sortOrder.asc);
  loadWeatherTable();
}

timeHeader.onclick = function(){ sortWeatherTable(0, timeHeader); }
tempHeader.onclick = function(){ sortWeatherTable(1, tempHeader); }
humHeader.onclick = function(){ sortWeatherTable(2, humHeader); }
pressHeader.onclick = function(){ sortWeatherTable(3, pressHeader); }

loadWeatherTable();
renderCaret(curHeader, true);

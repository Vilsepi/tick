
function httpGet(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() { 
    if (xhr.readyState == 4 && xhr.status == 200)
      callback(xhr.responseText);
  }
  xhr.open("GET", url, true);
  xhr.send(null);
};


/*
G https://www.nordnet.fi/graph/instrument/24/127211?from=2017-11-16&to=2017-11-16&fields=last,open,high,low,volume
V https://www.nordnet.fi/graph/instrument/24/145875?from=2017-11-16&to=2017-11-16&fields=last,open,high,low,volume
*/

var url = 'https://www.nordnet.fi/graph/instrument/24/127211?from=2017-11-16&to=2017-11-16&fields=last,open,high,low,volume';

httpGet(url, function(response) {
  var data = JSON.parse(response);
  var itemsDiv = document.getElementById('items')
  for(var i=0; i < data.length; i++) {
    var item = '<div class="item">' + data[i] + '</div>';
    itemsDiv.innerHTML = itemsDiv.innerHTML + item;
  }
});

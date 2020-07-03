let obj
const url = '/data/devices'
const request = async () => {
  const response = await fetch(url).catch((err) => console.log('Error:'. err))
  const json = await response.json();
  obj = JSON.parse(json);
  append_data(obj)
}
request();

function append_data (obj){

//console.log(obj)
for (var i = 0; i < obj.length; i++) {
  $("#devices").append("<option value="+obj[i].pk+">"+obj[i].fields.text+"</option>");
}
}
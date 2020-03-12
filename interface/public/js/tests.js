// FOr tests only
let data = {object: "music", toggle: "on"};

fetch("/webapp/api", {
  method: "POST", 
  body: JSON.stringify(data),
  headers:{
    'Content-Type': 'application/json'
  }
}).then(res => {
  console.log("Request status ", res.status);
});
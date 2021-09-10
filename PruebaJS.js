//curl -X GET \
//let apiKey = "wzt7BjBZhuafsjAM4wAl7G5tQqAHlPcCRwacvMHIY5U";
//let url1 = 'https://router.hereapi.com/v8/routes?origin=50.971173,1.900859&destination=50.96035,1.905025&return=summary,typicalDuration&transportMode=car&apikey='

//url = url1 + apiKey;


function httpGet(origin,destination){
    //console.log(origin)
    let lat_ori = origin[0].toString();
    let lon_ori = origin[1].toString();
    let lat_des = destination[0].toString();
    let lon_des = destination[1].toString();
    let apiKey = "wzt7BjBZhuafsjAM4wAl7G5tQqAHlPcCRwacvMHIY5U";

    let theUrl = 'https://router.hereapi.com/v8/routes?origin=' + lat_ori + ',' + lon_ori + '&destination=' + lat_des + ',' + lon_des + '&return=summary,typicalDuration&transportMode=car&apikey=' + apiKey;
    
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function extractDuration (st){
    let num = "";
    for(let i=0; i<st.length;i++){
        if(st.slice(i,i+8) == "duration"){
            //console.log(st.slice(i+10,i+12));
            let j = i + 10;
            while(st[j] != "," && st[j] != "\"" && st[j] != "," && st[j] != " "){
                num += st[j];
                j += 1;
            }
            break;
        }
       
    }
    
    return num; 
}

st = httpGet([17.066,-96.725555556],[17.071,-96.708333333]); //Peticion a la API

console.log(extractDuration(st)); //Obtener duracion

let mysql = require('mysql');

/*
let con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "12345678"
});

con.connect(function(err) {
if (err) throw err;
console.log("Connected!");
});
*/
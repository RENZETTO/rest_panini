const express = require("express")
const mysql = require('mysql');
var js2xmlparser = require("js2xmlparser");

let app = express()

let con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database : 'educazione_alimentare'
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
});

app.get("/api/ordinazioni/list", (req, res) => {
    type = ""
    switch (req.query['format'])
    {
        case "xml":
            res.setHeader("Content-Type", "application/xml")
            type = "xml"
        break;
        default:
            res.setHeader("Content-Type", "application/json")
            type = "json"
    }

    con.query('SELECT * FROM ordinazioni', function (error, results, fields) {
        if (error) throw error;
        risposta = results
        if(type == "xml"){
            risposta = js2xmlparser.parse("ordinazioni", results)
        }
        res.send(risposta)
    });
    
})

app.listen("3000")
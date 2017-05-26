var nats = require('nats').connect({'servers':['nats:iot-msg:4222']});
var express = require('express');
var http = require('http');
var redis = require('redis');

var app = express();
var client = redis.createClient('6379', 'rep-data');

nats.subscribe('create_project', function(msg) {
    var rep = JSON.parse(msg);
    client.set(rep.name, rep.host);
    console.log('Saved report: ' + msg);
});

app.get('/reports/:name', function(req, res) {
    client.get(req.params.name, function(err, reply) {
        if (reply==null) {
            res.statusCode = 404;
            return res.send('Error: Trash Can not found\n');
        }
        console.log(reply);
        res.send('{"name":"' + req.params.name + '", "host":"'
        + reply + '"}');
    });
});

app.put('/reports/:name', function(req, res) {
    client.put(req.params.name, function(err, reply) {
        if (reply==null) {
            res.statusCode = 404;
            return res.send('Error: Trash Can not found\n');
        }
        console.log(reply);
        res.send('{"name":"' + req.params.name + '", "host":"'
        + reply + '"}');
    });
});

http.createServer(app).listen(9090, function() {
    console.log('Listening on port 9090');
});
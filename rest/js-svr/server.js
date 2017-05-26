var express = require('express');
var http = require('http');
var program = require('commander');

var app = express();

//Parse command line args
program
  .option('-p, --port <n>', 'Port', parseInt, 9090)
  .parse(process.argv);

//Create routes
app.get('/projects/:name', function(req, res) {
    res.send('{"name":"' + req.params.name + '","host":"ASF","inception":"{"year":"2007","month":"1","day":"10"}"}');
});

app.put('/projects/:name', function(req, res) {
    res.send('{"code":"200","message":"ok"}');
});

//Run server
http.createServer(app).listen(program.port, function() {
    console.log('[Server] Listening on port ' + program.port);
});

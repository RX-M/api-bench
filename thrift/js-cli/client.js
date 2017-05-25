var thrift = require('thrift');
var helloSvc = require('./gen-nodejs/Projects.js');

var connection = thrift.createConnection('localhost', 9090, {
   transport: thrift.TBufferedTransport,
   protocol: thrift.TCompactProtocol
}).on('error', function(error) {
   console.log(error);
}).on("connect", function() {
   var client = thrift.createClient(Projects, connection);
   client.get("Thrift", function(error, result) {
      //console.log("Msg from server: " + result);
  });
  connection.end();
});


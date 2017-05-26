#!/usr/bin/env node

var thrift = require('thrift');
var Projects = require('./gen-nodejs/Projects.js');
var ProjectsTypes = require('./gen-nodejs/project_types.js');
var program = require('commander');

//Parse command line
program
  .option('-H, --host [value]', 'Host', 'localhost')
  .option('-p, --port <n>', 'Port', parseInt, 9090)
  .option('-a, --action <n>', 'Action (must be 1-3)', parseInt, 1)
  .parse(process.argv);

var connection = thrift.createConnection(program.host, program.port, {
   transport: thrift.TBufferedTransport,
   protocol: thrift.TCompactProtocol
}).on('error', function(error) {
   console.log(error);
}).on("connect", function() {
   console.log("[Client] Host " + program.host + ", Port " + program.port + ", Action " + program.action);
   var i = 0;
   var client = thrift.createClient(Projects, connection);
   //Get
   var cbGet = function(error, result) {
     i++;
     if (i < 1000000) {
       client.get("Thrift",cb); 
     } else {
       connection.end();
     }
   };
   client.get("Thrift", cbGet);
   //Create
   var cbCreate = function(error, result) {
     i++;
     if (i < 1000000) {
       client.create("Thrift",cb); 
     } else {
       connection.end();
     }
   };
   client.get("Thrift", cbGet);
   //Create/Get
   var cbCreateGet = function(error, result) {
     i++;
     if (i < 1000000) {
       client.get("Thrift",cb); 
     } else {
       connection.end();
     }
   };
   client.get("Thrift", cbGet);
});


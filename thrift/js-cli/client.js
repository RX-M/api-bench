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

var proj = ProjectsTypes.Project({name: 'Thrift', host: 'ASF', inception: {year: 2007, month: 1, day: 10}})

var connection = thrift.createConnection(program.host, program.port, {
   transport: thrift.TBufferedTransport,
   protocol: thrift.TCompactProtocol
}).on('error', function(error) {
   console.log(error);
}).on("connect", function() {
   var i = 0;
   var client = thrift.createClient(Projects, connection);
   switch (program.action) {
      case 1:   //Get
         var cbGet = function(error, result) {
            i++;
            if (i < 1000000) {
               client.get("Thrift", cbGet); 
            } else {
               connection.end();
            }
         };
         client.get("Thrift", cbGet);
         break;

      case 2:   //Create
         var cbCreate = function(error, result) {
            i++;
            if (i < 1000000) {
               client.create(proj, cbCreate); 
            } else {
               connection.end();
            }
         };
         client.create(proj, cbCreate);
         break;

      case 3:   //Create/Get
         var cbCreateGetC = function(error, result) {
               client.get("Thrift", cbCreateGetG); 
         }
         var cbCreateGetG = function(error, result) {
            i++;
            if (i < 1000000) {
               client.create(proj, cbCreateGetC); 
            } else {
               connection.end();
            }
         };
         client.create(proj, cbCreateGetC);
         break;
   }
});

console.log("[Client] Host " + program.host + ", Port " + program.port + ", Action " + program.action);


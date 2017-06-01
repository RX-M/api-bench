#!/usr/bin/env node

var thrift = require('thrift');

var Projects = require('./gen-nodejs/Projects.js');
var ProjectsTypes = require('./gen-nodejs/project_types.js');

var proj = ProjectsTypes.Project({name: 'Thrift', host: 'ASF', inception: {year: 2007, month: 1, day: 10}})

//Project Handler
var ProjectsHandler = {
  get: function(name, result) {
    result(null, new ProjectsTypes.Project({name: 'Thrift', host: 'ASF', inception: {year: 2007, month: 1, day: 10}}));
  },

  create: function(proj, result) {
    result(null, new ProjectsTypes.CreateResult({code: 0, msg: "ok"}), null);
  }
};

//Setup and run the server
var port = 9090;
thrift.createServer(Projects,
                    ProjectsHandler, 
                    { protocol: thrift.TCompactProtocol,
                      transport: thrift.TBufferedTransport })
   .on("error", function(e){ console.log(e); })
   .listen(port);
console.log("[Server] Listening on port " + port);



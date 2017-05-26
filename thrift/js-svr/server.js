#!/usr/bin/env node

var thrift = require('thrift');
var Projects = require('./gen-nodejs/Projects.js');
var ProjectsTypes = require('./gen-nodejs/project_types.js');
var program = require('commander');

//TradeHistory Handler
var ProjectsHandler = {
  Get: function(name, result) {
      result(new tradeTypes.BadFish({fish: “”, error_code: 5}), null);
  },

  Create: function(proj, result) {
      result(null, new tradeTypes.BadFish({fish: "", error_code: 5}), null);
  }
};

//Setup and run the server
var port = 9090;
thrift.createServer(tradeHistory,
                    ProjectsHandler, 
                    { protocol: thrift.TCompactProtocol,
                      transport: thrift.TBufferedTransport })
   .on(“error”, function(e){ console.log(e); })
   .listen(port);
console.log("[Server] Listening on port " + port);


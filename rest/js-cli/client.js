var http = require('http');
var program = require('commander');

//Parse command line args
program
  .option('-H, --host [value]', 'Host', '127.0.0.1')
  .option('-p, --port <n>', 'Port', 9090)
  .option('-a, --action <n>', 'Action (must be 1-3)', "1")
  .parse(process.argv);

var get_options = {
  hostname: program.host,
  port: program.port,
  path: '/projects/thrift',
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

var put_options = {
  hostname: program.host,
  port: program.port,
  path: '/projects/thrift',
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  }
};

console.log("[Client] Host " + program.host + ", Port " + program.port + ", Action " + program.action);

var requests = 1000000;
var i = 0;

switch (program.action) {

  case "1":

    var get = function(error, result) {
      i++;
      if (i < requests) {
        http.get(get_options, get); 
      } else {
        return
      }
    };
    http.get(get_options, get); 
    break;
  
  case "2": 

    var create = function(error, result) {
      i++;
      if (i < requests) {
          http.request(put_options, create).end();
      } else {
        return;
      }
    };
    http.request(put_options, create).end(); 
    break;
  
  case "3":

    var create_get = function(error, result) {
        http.get(get_options, crate_get);
    }
    var create_get = function(error, result) {
      i++;
      if (i < requests) {
        http.request(put_options, create_get).end();
      } else {
        return;
      }
    };
    http.request(put_options, create_get).end();
    break;
}

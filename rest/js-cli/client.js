var http = require('http');
var program = require('commander');

//Parse command line args
program
  .option('-H, --host [value]', 'Host', 'localhost')
  .option('-p, --port <n>', 'Port', parseInt, 9090)
  .option('-a, --action <n>', 'Action (must be 1-3)', parseInt, 1)
  .parse(process.argv);

var requests = 5;

function test(options){
	for (i = 0; i < requests; i ++){

		http.request(options, function(res) {
		  res.setEncoding('utf8');
		  res.on('data', function (chunk) {
		  });
		}).end();	
	}
}

function get_create_test(option1, option2){
	for (i = 0; i < requests; i ++){

		//get
		http.request(option1, function(res) {
		  res.setEncoding('utf8');
		  res.on('data', function (chunk) {
		  });
		}).end();

		//create
		http.request(option2, function(res) {
		  res.setEncoding('utf8');
		  res.on('data', function (chunk) {
		  });
		}).end();
	}
}

const get_options = {
  hostname: program.host,
  port: program.port,
  path: '/projects/Thrift',
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

const put_options = {
  hostname: program.host,
  port: program.port,
  path: '/projects/Thrift',
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  }
};

console.log("[Client] Host " + program.host + ", Port " + program.port + ", Action " + program.action);

switch (program.action) {

	case 1 :
		test(get_options);
		break;
	case 2: 
		test(put_options);	
		break;
	case 3:
		get_create_test(get_options, put_options);
		break;
}

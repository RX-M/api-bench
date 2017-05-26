var servers = ['nats:iot-msg:4222'];
var topic = 'project';
var nats = require('nats').connect({'servers':servers});
var requests = 100;

function get_test(name) {
	for (i = 0; i < requests; i ++){

	}
}

function create_test(name) {
	for (i = 0; i < requests; i ++){
	    msg = '{"name":"'+ name + '", "host":"ASF", "inception":' + 
	    '{"day":"10", "month":"10", "year":2007}}';
	    console.log("Creating " + name);
	    nats.publish(topic, msg);
	}
}

// process.argv.forEach(function (val, index, array) {
//   console.log(index + ': ' + val);
// });

if (process.argv[3] == 1) {
	//get_test();
}

else if (process.argv[3] == 2) {
	create_test("Thrift");
}

else {
	//get_create_test();
}
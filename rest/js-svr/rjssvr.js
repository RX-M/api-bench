var servers = ['nats:iot-msg:4222'];
var topic = 'trash-level';
var nats = require('nats').connect({'servers':servers});

function trash_level() {
    var lvl = Math.random() * 100;
    var can_id = (Math.random() * 1000).toFixed();
    msg = '{"can_id":"' + can_id + '", "level":"' + lvl + '"}';
    console.log('publishing: ' + msg);
    nats.publish(topic, msg);
}

setInterval(trash_level, 4000);
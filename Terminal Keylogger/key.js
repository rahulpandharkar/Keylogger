const keypress = require('keypress');
const axios = require('axios');

keypress(process.stdin);
process.stdin.on('keypress', function (ch, key) {
  console.log(key);
  sendData(key);
  if (key.sequence === 'N') {
    process.exit(0);
  }
});

process.stdin.setRawMode(true);
process.stdin.resume();

function sendData(key) {
  const serverUrl = 'http://192.168.1.10:5000';
  axios.post(serverUrl, { key })
    .then(response => {
      console.log('Data sent to the server:', response.data);
    })
    .catch(error => {
      console.error('Error sending data:', error.message);
    });
}
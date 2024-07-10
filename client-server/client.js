const request = require('request');
request('https://yakimhsu.com',
  function (error, response, body) {
    console.error('error:', error);
    console.log('statusCode:', response && response.statusCode);
    console.log('head:', response.headers); // 多印 response 的 header
    console.log('body:', body);
});
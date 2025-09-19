const https = require('express');
const fs = require('fs');


openssl req -nodes -new -x509 -keyout key.pem -out cert.pem
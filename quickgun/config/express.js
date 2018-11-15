const express = require('express');
const morgan = require('morgan');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const {
  debugInit,
} = require('helpers/debugger');


const shoot = require('app/shoot');


// const debugDb = makeLogger('app:database');
// create express server
const server = express();
const router = express.Router();


server.use(morgan('dev', { stream: { write: msg => debugInit(msg) } }));


// parse body params and attache them to req.body
server.use(bodyParser.json());
server.use(bodyParser.urlencoded({ extended: true }));

// cookie par
server.use(cookieParser());

router.post('/shoot', shoot);


router.get('/', (req, res) => {
  res.send("Shoot'em up");
});


server.use(router);

module.exports = server;

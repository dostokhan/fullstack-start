const express = require('express');

const {
  debugInit,
} = require('helpers/debugger');



/**
 * Express configuration.
 */
const server = require('config/express');


server.listen(4200, () => {
  debugInit(`NODE_ENV: ${process.env.NODE_ENV}`);
  debugInit('we are ready :)');
});

const express = require('express');

const {
  debugInit,
} = require('helpers/debugger');

const {
  port,
  nodeEnv,
} = require('config/vars');


/**
 * Express configuration.
 */
const server = require('config/express');


server.listen(port, () => {
  debugInit(`NODE_ENV: ${nodeEnv}`);
  debugInit('we are ready :)');
});

const {
  debugCommon,
  debugError,
} = require('helpers/debugger');


const shoot = (req, res) => {
  debugCommon('Shoot');

  res.send(200);
};

module.exports = shoot;

const debug = require('debug');

const debugInit = debug('app:init');
const debugError = debug('app:error');
const debugCommon = debug('app:common');


module.exports = {
  debugInit,
  debugError,
  debugCommon,
};

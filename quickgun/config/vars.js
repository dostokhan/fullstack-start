const path = require('path');
const dotenv = require('dotenv');

const projectRoot = path.join(__dirname, '../');
dotenv.load({ path: `${projectRoot}.env` });


module.exports = {
  projectRoot,
  nodeEnv: process.env.NODE_ENV,
  port: process.env.PORT,
  secret: process.env.SECRET,
};

const childProcess = require('child_process');
const {
  debugCommon,
  debugError,
} = require('helpers/debugger');


const deploy = (res, branch) => {
  const nodeEnv = process.env.NODE_ENV;
  childProcess.exec(`cd ./../ && ./deploy.py ${branch} ${nodeEnv}`, function(err, stdout, stderr){
    if (err) {
      console.error(err);
      return res.send(500);
    }
    res.send(`Deployed ${branch}`);
  });
};

const shoot = (req, res) => {
  const sender = req.body.sender;
  const branch = req.body.ref;
  debugCommon(`Sender: ${sender}`);
  debugCommon(`Brach: ${branch}`);

  if(branch.indexOf('release') > -1){
    deploy(res, branch);
  } else {
    res.send(`Not Deploying ${branch}`);
  }
};

module.exports = shoot;

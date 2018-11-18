const childProcess = require('child_process');
const crypto = require('crypto');
const path = require('path');

const {
  debugCommon,
  debugError,
} = require('helpers/debugger');
const {
  secret,
  nodeEnv,
  projectRoot,
} = require('config/vars');


const verifyGitHub = (req) => {
  const theirSignature = req.get('X-Hub-Signature');
  const payload = JSON.stringify(req.body);
  const ourSignature = `sha1=${crypto.createHmac('sha1', secret).update(payload).digest('hex')}`
  return crypto.timingSafeEqual(Buffer.from(theirSignature), Buffer.from(oursignature));
};

const deploy = (res, branch) => {
  const rootPath = path.join(projectRoot, '../');
  const cmd = `cd ${rootPath} && ./deploy.py ${branch} ${nodeEnv}`;
  debugCommon(`cmd: ${cmd}`);

  childProcess.exec(cmd, function(err, stdout, stderr){
    if (err) {
      debugError(err);
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
    if (verifyGitHub(req)) {
      deploy(res, branch);
    } else {
      debugError('Secret missmatch!');
    }
  } else {
    res.send(`Not Deploying ${branch}`);
  }
};

module.exports = shoot;

const DDoSDefense = artifacts.require("DDoSDefense");

module.exports = function (deployer) {
  deployer.deploy(DDoSDefense);
};

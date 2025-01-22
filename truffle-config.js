module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",     // Localhost
      port: 8545,            // Port for Ganache CLI
      network_id: "*"        // Match any network id
    }
  },
  compilers: {
    solc: {
      version: "0.8.0"       // Ensure it matches the Solidity version in your contract
    }
  }
};

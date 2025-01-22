// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DDoSDefense {
    address public owner;
    mapping(string => bool) private blacklist;

    event IPBlacklisted(string ip);
    event IPWhitelisted(string ip);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function addToBlacklist(string memory ip) public onlyOwner {
        require(!blacklist[ip], "IP already blacklisted");
        blacklist[ip] = true;
        emit IPBlacklisted(ip);
    }

    function removeFromBlacklist(string memory ip) public onlyOwner {
        require(blacklist[ip], "IP not in blacklist");
        blacklist[ip] = false;
        emit IPWhitelisted(ip);
    }

    function isBlacklisted(string memory ip) public view returns (bool) {
        return blacklist[ip];
    }
}

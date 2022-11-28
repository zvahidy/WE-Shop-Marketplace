pragma solidity ^0.5.5;

import "./kikeCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/WhitelistCrowdsale.sol";
// Have the KikeCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
// * WhitelistCrowdsale
// * CappedCrowdsale
// * RefundablePostDeliveryCrowdsale

contract kikeCoinCrowdsale is Crowdsale, MintedCrowdsale ,WhitelistCrowdsale,CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale{ // UPDATE THE CONTRACT SIGNATURE TO ADD INHERITANCE
//contract kikeCoinCrowdsale is Crowdsale, MintedCrowdsale,CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale{ // UPDATE THE CONTRACT SIGNATURE TO ADD INHERITANCE    
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate,
        address payable wallet, // sale beneficiary
        kikeCoin token, // The kikeCoin itself that the kikeCoinCrowdsale will work with,
        uint goal, // The crowdsale goal
        uint open, // The crowdsale opening time
        uint close // The crowdsale closing time
        
    ) 
        //Crowdsale(rate, wallet, token)
        public 
        Crowdsale(rate, wallet, token)
        CappedCrowdsale(goal)
        TimedCrowdsale(open,close)
        RefundableCrowdsale(goal)
        
    
    {
        // constructor can stay empty
    }
}

contract KikeCoinCrowdsaleDeployer {
    // Create an `address public` variable called `kike_token_address`.
    
    address public kike_token_address;
    
    // Create an `address public` variable called `kike_crowdsale_address`.
    
    address public kike_crowdsale_address;
    // Add the constructor.
    constructor(
       string memory name,
       string memory symbol,
       address payable wallet,
       uint goal
    ) public {
        // Create a new instance of the kikeCoin contract.
        kikeCoin token = new kikeCoin(name, symbol,0);

        // Assign the token contract’s address to the `kike_token_address` variable.
        kike_token_address = address(token);

        // Create a new instance of the `kikeCoinCrowdsale` contract
        //kikeCoinCrowdsale kike_crowdsale = new kikeCoinCrowdsale (1, wallet, token, goal, now, now + 24 weeks);
        kikeCoinCrowdsale kike_crowdsale = new kikeCoinCrowdsale (1, wallet, token, goal, now, now + 50 minutes);

        // Aassign the `kikeCoinCrowdsale` contract’s address to the `kike_crowdsale_address` variable.
        kike_crowdsale_address = address(kike_crowdsale);

        // Set the `kikeCoinCrowdsale` contract as a minter
        token.addMinter(kike_crowdsale_address);

        // Have the `kikeCoinCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}
pragma solidity ^0.5.0;

contract Transaction {
    //address payable buyer; //holds ethereum address of buyer
    //address payable seller; //holds ethereum address of seller
    uint public accountBalance;
    function transfer(uint amount, address payable recipient) public {
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
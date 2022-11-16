import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./artifacts/Transaction_metadata.json')) as f:
        artwork_abi = json.load(f)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    print(contract_address)
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi['output']['abi']
    )
    return contract

contract = load_contract()
accounts = w3.eth.accounts
option = st.selectbox('Which account would you like to pay with', options=accounts)
to_address = "0x6a7F0Cc12f30C905C3139395aC1Bbf7c294e9dcd"
if st.button("Pay"):
    contract.functions.deposit().transact({
        "from": option,
        'value': 1000000000000000000
    })
    contract.functions.transfer(1000000000000000000, to_address).transact({
        "from": option
    })
    st.write("Success!!!")


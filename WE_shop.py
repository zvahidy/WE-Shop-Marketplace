# WE Shop Marketplace (WE stand together for Women Empowerment)

# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List




# From wallet.py import the functions w3, generate_account, get_balance

from crypto_wallet import w3, generate_account, get_balance

################################################################################
# WE shop merchandise (Tshirts)

# Database of Shirts including their name, digital address, rating and in Ether.
# A single Ether is currently valued at (look up current value)

WE_database = {
    "Fundamentals": ["Fundamentals", .05],
    "The Riviter": ["The Riviter", .06],
    "RBG": ["RBG", .07],
    "Codess": ["Codess", .08]
}

# Create a list of the shirt names/type
Shirt = ["Fundamentals", "Rosie", "RBG"]

# Create a get_WE function to display the purchase information from the WE_database
def get_WE():
    """Display the database of cats to purchase information."""
    db_list = list(WE_database.values())

    for number in range(len(Shirt)):
        st.write("Name: ", db_list[number][0])
        st.write("Price in Ether: ", db_list[number][1], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Create Streamlit application headings using `st.markdown` to explain this app is for buying shirts
st.markdown("# WE stand together for Women Empowerment")
st.markdown("## Buy a WE Tee!")
st.text(" \n")

#
#
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)
#  Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(w3, account.address)

# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")

# Create a select box to chose a Shirt using `st.sidebar.selectbox`
Shirt = st.sidebar.selectbox('Select a Shirt', Shirt)

#  Create a header using ` st.sidebar.markdown()` to display Shirt name and price.
st.sidebar.markdown("## Shirt Name and Price")

# Identify the Shirt for purchase by name
Shirt = WE_database[Shirt][0]

# Create a variable called `Shirt_price` to retrive the cat price from the `WE_database` using block notation.
Shirt_price = WE_database[Shirt][1]

# Use a conditional statement using the `if` keyword to check if the selected Shirt can be purchased. This will be done by checking the user's account balance that wishes to make the purchase.
if Shirt_price <= ether:
  new_balance = float(ether) - float(Shirt_price)
# Write the Shirt name to the sidebar
  st.sidebar.write("If you buy", Shirt, "for", Shirt_price, "eth, your account balance will be", new_balance, ".")
  get_WE()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", Shirt, "for", Shirt_price, "eth." )
  get_wE()

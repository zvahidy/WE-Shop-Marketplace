# Imports
import streamlit as st
import sqlite3
from dataclasses import dataclass
from typing import Any, List




# From wallet.py import the functions w3, generate_account, get_balance

from crypto_wallet import w3, generate_account, get_balance

################################################################################
# WE shop merchandise (Tshirts)

# Database of Shirts including their name, digital address, rating and in Ether.
# A single Ether is currently valued at (look up current value)

conn = sqlite3.connect('we1.db')
engine = conn.cursor()

select_all_data = """
SELECT * FROM shop
"""

select_shirt_names = """
  select shirt_name from shop
"""


engine.execute(select_all_data)
we_shop_database = engine.fetchall()

# Create a list of the shirt names/type
shirts = []
for x in list(we_shop_database):
  shirts.append(x[1])


# Create a get_WE function to display the purchase information from the WE_database
def get_shirts():
    """Display the database of cats to purchase information."""
    db_list = we_shop_database

    for number in range(len(db_list)):
        st.write("Name: ", db_list[number][1])
        st.write("Price in Ether: ", db_list[number][2], "eth")
        st.image(db_list[number][3])
        st.text(" \n")

################################################################################
# Streamlit Code

# Create Streamlit application headings using `st.markdown` to explain this app is for buying shirts
st.markdown("# WE stand together for Women Empowerment #")
st.markdown("## Buy a WE Tee! ##")
st.write("All proceeds are donated to the NEEMA PROJECT. Click here to learn more https://www.neemaproject.org")

st.text(" \n")

#
#
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account(w3)
#  Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(w3, account.address)

# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether ##")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")

# Create a select box to chose a Shirt using `st.sidebar.selectbox`
shirt = st.sidebar.selectbox('Select a Shirt', shirts)

#  Create a header using ` st.sidebar.markdown()` to display Shirt name and price.
st.sidebar.markdown("## Shirt Name and Price")

# Identify the Shirt for purchase by name
select_specific_shirt = "SELECT * FROM shop WHERE shirt_name = '{}'".format(shirt)
engine.execute(select_specific_shirt)
shirt_info = engine.fetchall()[0]

#shirt = we_shop_database[shirt][1]

# Create a variable called `Shirt_price` to retrive the cat price from the `WE_database` using block notation.
shirt_price = shirt_info[2]

# Use a conditional statement using the `if` keyword to check if the selected Shirt can be purchased. This will be done by checking the user's account balance that wishes to make the purchase.
if shirt_price <= ether:
  new_balance = float(ether) - float(shirt_price)
# Write the Shirt name to the sidebar
  st.sidebar.write("If you buy", shirt, "for", shirt_price, "eth, your account balance will be", new_balance, ".")
  get_shirts()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", shirt, "for", shirt_price, "eth." )
  get_shirts()






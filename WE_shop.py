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

we_shop_database = {
    "Fundamentals": ["Fundamentals", .05, "https://images-na.ssl-images-amazon.com/images/I/71Zg2d9QG2S._AC_UX466_.jpg"],
    "Rosie The Riviter": ["Rosie The Riviter", .06, "https://m.media-amazon.com/images/I/A13usaonutL._CLa%7C2140%2C2000%7C918Dsd9GtiL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_UX679_.png"] ,
    "RBG": ["RBG", .07, "https://i.etsystatic.com/36271525/r/il/d3b13d/4006850366/il_1588xN.4006850366_sys0.jpg"],
    "Codess": ["Codess", .08, "https://res.cloudinary.com/teepublic/image/private/s--adJ33DFv--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,h_576/c_crop,g_north_west,h_626,w_470,x_-39,y_-25/g_north_west,u_upload:v1462829024:production:blanks:a59x1cgomgu5lprfjlmi,x_-434,y_-350/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1589371695/production/designs/10105194_0.jpg"],
}

# Create a list of the shirt names/type
shirts = ["Fundamentals", "Rosie The Riviter", "RBG", "Codess"]

# Create a get_WE function to display the purchase information from the WE_database
def get_shirts():
    """Display the database of cats to purchase information."""
    db_list = list(we_shop_database.values())

    for number in range(len(shirts)):
        st.write("Name: ", db_list[number][0])
        st.write("Price in Ether: ", db_list[number][1], "eth")
        st.image(db_list[number][2])
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
shirt = we_shop_database[shirt][0]

# Create a variable called `Shirt_price` to retrive the cat price from the `WE_database` using block notation.
shirt_price = we_shop_database[shirt][1]

# Use a conditional statement using the `if` keyword to check if the selected Shirt can be purchased. This will be done by checking the user's account balance that wishes to make the purchase.
if shirt_price <= ether:
  new_balance = float(ether) - float(shirt_price)
# Write the Shirt name to the sidebar
  st.sidebar.write("If you buy", shirt, "for", shirt_price, "eth, your account balance will be", new_balance, ".")
  get_shirts()
else:
  st.sidebar.write("With a balance of", ether, "ether, you can't buy", shirt, "for", shirt_price, "eth." )
  get_shirts()


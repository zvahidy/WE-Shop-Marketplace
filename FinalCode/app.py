from flask import Flask, render_template, request, url_for
import sqlite3
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import os
import json
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
load_dotenv()



def load_contract(w3):
    with open(Path('./artifacts/Transaction_metadata.json')) as f:
        artwork_abi = json.load(f)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi['output']['abi']
    )
    return contract

def purchase_item(w3, contract, engine, conn, item_info, item_type, from_address):
  
  price_in_wei = w3.toWei(item_info[2], "ether")
  if item_type == "Tee-shirts":
    decrement_item_count = """
    UPDATE shop
    SET item_count=item_count-1
    WHERE shirt_name='{}';
    """.format(item_info[1])
  else:
    decrement_item_count = """
    UPDATE stationery
    SET item_count=item_count-1
    WHERE item_name='{}';
    """.format(item_info[1])

  if(item_info[4] <= 0):
    print("Item sold out")
    return -1
  else:
    engine.execute(decrement_item_count)
    conn.commit()
    contract.functions.deposit().transact({
        "from": from_address,
        'value': price_in_wei
    })
    contract.functions.transfer(price_in_wei, item_info[5]).transact({
        "from": from_address
    })
    return 1

class PurchaseForm(FlaskForm):
    purchaser = SelectField('Please Select Address you want to pay with:')
    item = SelectField('Select Item Name:')
    item_type = SelectField('Select Item Type')
    quantity= IntegerField('Select Qty:')
    submit = SubmitField('Purchase Item')

@app.route("/", methods=['GET', 'POST'])
def hello():
    test_var = 0
    w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
    contract = load_contract(w3)
    accounts = w3.eth.accounts

    conn = sqlite3.connect('we1.db')
    engine = conn.cursor()
    select_all_data = """
    SELECT * FROM shop
    """
    select_shirt_names = """
    select shirt_name from shop
    """
    engine.execute(select_all_data)
    we_shirt_database = engine.fetchall()

    select_stationery_data = """
    SELECT * FROM stationery
    """

    engine.execute(select_stationery_data)
    we_stationery_database = engine.fetchall()

    shirts = []
    for x in list(we_shirt_database):
      shirts.append(x[1])

    stationery = []
    for x in list(we_stationery_database):
      stationery.append(x[1])

    data_for_page = {
      'accounts': accounts,
      'img_data': [list(i) for i in we_shirt_database],
      'stationery_data': [list(i) for i in we_stationery_database]
    } 


    form = PurchaseForm()
    form.purchaser.choices = accounts
    form.item_type.choices = ['Tee-shirts', 'Stationery']
    form.item.choices = shirts
    if form.is_submitted():
      form_results= (request.form).to_dict(flat=False)
      print(form_results['item'][0])
      select_specific_shirt = "SELECT * FROM shop WHERE shirt_name = '{}'".format(form_results['item'][0])
      engine.execute(select_specific_shirt)
      shirt_info = engine.fetchall()[0]
      if form_results['item_type'][0] == "Tee-shirts":
        select_specific_item = "SELECT * FROM shop WHERE shirt_name = '{}'".format(form_results['item'][0])
      else:
        select_specific_item = "SELECT * FROM stationery WHERE item_name = '{}'".format(form_results['item'][0])
      engine.execute(select_specific_item)
      item_info = engine.fetchall()[0]

      print(item_info)
      test_var = purchase_item(w3, contract, engine, conn, item_info, form_results['item_type'][0], form_results['purchaser'][0])

    
    return render_template('index.html', data=data_for_page, form=form, test_var=test_var)

@app.route('/KikeCoin.html')
def display():
  return render_template('token.html')
    
    
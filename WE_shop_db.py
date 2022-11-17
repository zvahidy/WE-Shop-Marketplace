import sqlite3
import streamlit as st
import math

conn = sqlite3.connect('we1.db')
engine = conn.cursor()

def get_shirts(): 
	results=list(engine.execute('SELECT shirt_name, shirt_price, link FROM shop'))
	max_columns=3
	rows=math.ceil(len(results)/max_columns)
	count=0
	for each_row in range(rows): 
		columns=st.columns(max_columns)
		for each_col in columns: 
			with each_col: 
				if count<len(results): 
					each_shirt=results[count]
					st.image(each_shirt[2], width=200)
					st.write(f'Name: {each_shirt[0]}')
					st.write(f'Price: {each_shirt[1]}')
					count+=1
				else: 
					break
			

get_shirts()

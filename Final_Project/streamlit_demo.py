"""
To run this app, in your terminal:
> streamlit run streamlit_demo.py

Source: https://is.gd/SobJvL
"""
import numpy
import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import urllib.request, json

# Loading model 
dt = joblib.load('./model/delivery_classifier.joblib')

# Create title and sidebar
st.title("Delivery Risk Classification App")
st.sidebar.title("Features")

order_addr = st.sidebar.text_input("Your address", 'New York City, USA', key='ads')
google_key = 'AIzaSyB6WY3zY0yDCl6ed1AJh3GyMhbszAQVi-k'
pre = 'https://maps.googleapis.com/maps/api/geocode/json?address='

def clear_text():
    st.session_state["ads"] = ""

# todo combine to getdict function
def get_loc():
	with urllib.request.urlopen(pre+order_addr.replace(' ', '%20')+google_key) as url:
		lst = []
		res = json.load(url)
		if len(res['results']) == 0:
			return None
		lc = res['results'][0]['geometry']['location']
		lst.append(lc['lat'])
		lst.append(lc['lng'])
		return lst

data = pd.read_csv('./data/data1.csv', header=0, encoding='latin-1')
def get_cate_option():
	dict_id_cat = data.set_index('Category Name').to_dict()['Category Id']
	return dict_id_cat

def get_ship_option():
	lst = []
	for t in data['Shipping Mode'].unique():
		lst.append(t)
	lst.sort()
	dict_id_ship = {}
	for i in range(len(lst)):
		dict_id_ship[lst[i]] = i
	return dict_id_ship



def get_market_option():
	lst = []
	for t in data['Market'].unique():
		lst.append(t)
	lst.sort()
	dict_id_mar = {}
	for i in range(len(lst)):
		dict_id_mar[lst[i]] = i
	return dict_id_mar

dict_id_cat = get_cate_option()
cate_option = st.sidebar.selectbox(
    'Product Category',
    list(dict_id_cat.keys()))

dict_id_mar = get_market_option()
market_option = st.sidebar.selectbox(
    'Market',
    list(dict_id_mar.keys()))

dict_id_ship = get_ship_option()
ship_option = st.sidebar.selectbox(
    'Shipping Mode',
    list(dict_id_ship.keys()))

st.write('\n\n')

# Button that triggers the actual prediction
if st.button("Click Here to Classify"):
	st.snow()
	lst = get_loc()
	if not lst:
		st.text('Wrong address, try to input again!')
	else:
		test_data = [lst[0], lst[1]]  #2

		# todo Electronic catgory got two ids, 13 and 37
		cat_ids = list(dict_id_cat.values())
		cat_ids.append(13)
		cat_ids.sort()
		for i in cat_ids:
			if i == dict_id_cat[cate_option]:
				test_data.append(1)
			else:
				test_data.append(0)
		for i in range(len(dict_id_mar)):
			if i == dict_id_mar[market_option]:
				test_data.append(1)
			else:
				test_data.append(0)
		for i in range(len(dict_id_ship)):
			if i == dict_id_ship[ship_option]:
				test_data.append(1)
			else:
				test_data.append(0)
		test_arr = numpy.array(test_data).reshape(1, -1)
		prediction = dt.predict(test_arr)
		st.text(prediction)
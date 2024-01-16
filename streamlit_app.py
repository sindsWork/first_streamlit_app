import streamlit
import pandas

streamlit.title('My parents new healthy Diners')
streamlit.header('Breakfast Menu')
streamlit.text('oatmeal')
streamlit.text('kale spinach smoothie')
streamlit.text('hard boiled egg')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
streamlit.header("Fruityvice Fruit Advice!")
import requests

streamlit.text(fruityvice_response)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)



                              

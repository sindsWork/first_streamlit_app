import streamlit
import pandas
streamlit.title('My parents new healthy Diners')
streamlit.header('Breakfast Menu')
streamlit.text('oatmeal')
streamlit.text('kale spinach smoothie')
streamlit.text('hard boiled egg')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)


                              

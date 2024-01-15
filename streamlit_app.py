import streamlit
import pandas
streamlit.title('My parents new healthy Diners')
streamlit.header('Breakfast Menu')
streamlit.text('oatmeal')
streamlit.text('kale spinach smoothie')
streamlit.text('hard boiled egg')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
                              

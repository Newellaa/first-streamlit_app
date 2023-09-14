import streamlit 

streamlit.title('Breakfast Favorites')

streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('Build Your Own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list  here to pick the fruit
#fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display Table
streamlit.dataframe(fruits_to_show)

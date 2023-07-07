import streamlit as sl

sl.title( 'My Parents New Healthy Diner' )

sl.header( 'Breakfast Favorites' )
sl.text( '🥣 Omega 3 & Blueberry Oatmeal' )
sl.text( '🥗 Kale, Spinach & Rocket Smoothie' )
sl.text( '🐔 Hard-Boiled Free-Range Egg' )
sl.text( '🥑🍞 Avocado Toast' )

sl.header( '🍌🥭 Build Your Own Fruit Smoothie 🥝🍇' )

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
sl.dataframe(my_fruit_list)

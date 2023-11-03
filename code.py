#importing the necessary libraries
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pymongo
from googleapiclient.discovery import build
from PIL import Image



# SETTING PAGE CONFIGURATIONS
icon = Image.open("Youtube_logo.png")
st.set_page_config(page_title= "Youtube Data Harvesting and Warehousing | By Nikita Y P",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This app is created by Nikita"""})

# CREATING OPTION MENU
with st.sidebar:
    selected = option_menu(None, ["Home","Extract and Transform","View"], 
                           icons=["house-door-fill","tools","card-text"],
                           default_index=0,
                           orientation="vertical",
                           styles={"nav-link": {"font-size": "30px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "#C80101"},
                                   "icon": {"font-size": "30px"},
                                   "container" : {"max-width": "6000px"},
                                   "nav-link-selected": {"background-color": "#C80101"}})

# Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
client = pymongo.MongoClient("mongodb://localhost:270/")
db = client['youtube_data']

# CONNECTING WITH MYSQL DATABASE
mydb = sql.connect(host="localhost",
                   user="root",
                   password="Deol1000%axy",
                   database= "youtube_db"
                  )
mycursor = mydb.cursor(buffered=True)

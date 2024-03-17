from streamlit_card import card
from navigation import make_sidebar
import streamlit as st
from datetime import date
import datetime
import sqlite3

make_sidebar()
today = date. today()
yesterday = today - datetime.timedelta(days=1)
day_before = yesterday - datetime.timedelta(days=1)
day_before_day = day_before - datetime.timedelta(days=1)
today = today. strftime("%d/%m/%Y")
yesterday = yesterday. strftime("%d/%m/%Y")
day_before = day_before.strftime("%d/%m/%Y")
day_before_day = day_before_day.strftime("%d/%m/%Y")
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns([6,3,2]) #just to highlight these are different cols

with st.container():
    c1.hasClicked = card(
  
  title= today,
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
  )
    
    c2.hasClicked = card(
  
  title= (yesterday),
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
  )
    c3.hasClicked = card(
  
  title= day_before,
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
 )  

with st.container():
    c4.hasClicked = card(
  
  title= day_before_day,
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
  )
    c5.hasClicked = card(
  
  title= (today+day_before_day),
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
  )
    c6.hasClicked = card(
  
  title= (today+day_before),
  text="Some description",
  image="http://placekitten.com/200/300",
  url="http://localhost:8501",
  styles={
        "card": {
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            
        },
        "text": {
            "font-family": "serif",
            
        }
    }
  )

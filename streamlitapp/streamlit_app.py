import json
import requests
import streamlit as st
import time
import elasticsearch
from st_pages import Page, show_pages, add_page_title

st.set_page_config(
    page_title = "luck4",
    page_icon = "🍀"
    
)

st.title("Search for Investors")

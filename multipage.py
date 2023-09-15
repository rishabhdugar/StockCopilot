"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st
from constants import *

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func, *args, **kwargs) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title, 
                "function": func,
                "args": args,
                "kwargs": kwargs
            }
        )

    def run(self):
        # Drodown to select the page to run  
        #st.sidebar.image('logo.jpeg', width=100)
        st.sidebar.title("Stock Copilot")
        st.sidebar.write("### Choose your profile")
        # Define the slider
        trader_type = st.sidebar.select_slider(
            'Select your risk appetite',
            [e.value for e in TRADER_TYPES]
        )
        
        st.sidebar.write(f'You selected {trader_type} risk portfolio.')
        
        investment_type = st.sidebar.radio('Investment type', [e.value for e in INVESTMENT_TYPES])
        
        st.sidebar.write(f'You selected {investment_type} investment.')
        
        selection = st.sidebar.selectbox(
            "Please select the stock for analysis",
            ["Select..."] + list(ALL_STOCKS.keys()),
        )

        page = st.sidebar.selectbox(
            'Select a page:', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        if selection and selection != "Select...":
            page['kwargs']['selection'] = selection

        if trader_type:
            page['kwargs']['trader_type'] = trader_type

        if investment_type:
            page['kwargs']['investment_type'] = investment_type

        # run the app function 
        page['function'](*page["args"], **page["kwargs"])
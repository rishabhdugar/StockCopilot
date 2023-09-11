"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st

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
        # st.sidebar.image('some-image.png', width=200)
        st.sidebar.title("Stock Copilot")
        st.sidebar.write("### Choose your profile")
        # Define the slider
        trader_type = st.sidebar.select_slider(
            'Select your risk appetite',
            ['Low', 'Medium', 'Aggressive']
        )
        
        st.sidebar.write(f'You selected {trader_type} risk portfolio.')
        
        investment_type = st.sidebar.radio('Investment type', ['Long Term', 'Short Term'])
        
        st.sidebar.write(f'You selected {investment_type} investment.')
        
        tab1, tab2, tab3 = st.tabs(["Know About Company", "Buy/Sell Recommendation", "Market Sentiment"])
        tab1.write("Know About Company tab")
        tab2.write("Buy/Sell Recommendation tab")
        tab3.write("Market Sentiment tab")

        #page = st.sidebar.selectbox(
        #    'Risk Type:', 
        #    self.pages, 
        #    format_func=lambda page: page['title']
        #)

        # run the app function 
        #page['function'](*page["args"], **page["kwargs"])
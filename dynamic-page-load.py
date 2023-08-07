import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dynamic Page Loading without a Multi-Page App")

sidebar = st.sidebar()

markdown = '''
["Link 1"](demo_pages/page.py)
'''

with sidebar:
  sidebar.markdown(markdown, unsage_allow_html=True)

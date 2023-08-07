import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dynamic Page Loading without a Multi-Page App")



markdown = '''
["Link 1"](demo_pages/page.py)
'''

with st.sidebar:
  st.markdown(markdown, unsage_allow_html=True)

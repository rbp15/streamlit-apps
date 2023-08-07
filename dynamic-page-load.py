import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dynamic Page Loading without a Multi-Page App")



markdown = '''
  ["Direct Load Link 1"](demo_pages/page.py)
'''

alternative_idea = '''
  ["Query String Load"](?load=page.py)
'''

with st.sidebar:
  st.markdown(markdown, unsafe_allow_html=True)
  st.divider()
  st.markdown(alternative_idea, unsafe_allow_html=True)
  st.text("All links load a url format such as: /~/+/?load=page.py")

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
  
st.header("Link target would load here, sidebar maintained, no reload?")
st.text('All links in sidebar currently load a url format such as: "/~/+/demo_pages/page.py" or "/~/+/?load=page.py"')
st.divider()
st.text('I don't want a multipage app because I need full control over the links in the left bar.  I have a search field that filters the navigation list - it's working')

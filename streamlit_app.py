import streamlit as st
name=st.text_input('ENTER NAME')
btn=st.button('show')
if btn:
  st.write(f'Hello {name}')

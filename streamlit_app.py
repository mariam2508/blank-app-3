import streamlit as st


st.sidebar.title('sidebar')
area=None
st.header("calculate area")
with st.sidebar :
  choose=st.selectbox('select shape',('circle','rectangle'))
if choose=='circle':
  r=st.number_input('enter r',min_value=1,max_value=100)
  area=3.14*r*r
  
elif choose =='rectangle':
  w=st.number_input('enter w',min_value=1,max_value=100)
  h=st.number_input('enter h',min_value=1,max_value=100)
  area=w*h
  
bt=st.button('calculate')
if bt:
  st.write(f'area={area}')

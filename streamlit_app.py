import streamlit as st

import pandas as pd
st.header(' file upload app')
file=st.file_uploader('upload file',type=['csv'])

if file is not None:
  df=pd.read_csv(file)
  st.write(df)

import streamlit as st

import pandas as pd
st.header(' file upload app')
file=st.file_uploader('upload file',type=['csv'])

if file is not None:
  df=pd.read_csv(file)
  st.write(df)
  num_row=st.slider('choose num rows',min_value=1,max_value=len(df))
  names_columns=st.multiselect('choose names of  columns',df.columns.tolist())
  if names_columns:
    st.write(df[:num_row][names_columns])
  else:
    st.write(df[:num_row])


x_col=st.selectbox('choose x',df.columns.tolist())
y_col=st.selectbox('choose y',df.columns.tolist())
fig=px.scatter(df,x=x_col,y=y_col)
st.plotly_chart(fig)

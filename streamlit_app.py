import streamlit as st
import plotly.express as px
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


num_col = df.select_dtypes(include='number').columns.tolist()

col1, col2, col3 = st.columns(3)

with col1:
    x_col = st.selectbox('Choose x-axis', num_col)
with col2:
    y_col = st.selectbox('Choose y-axis', num_col)
with col3:
    color = st.selectbox('Choose color', num_col)

plot_type = st.selectbox('Choose plot type', ['Scatter Plot', 'Histogram'])

if plot_type == 'Scatter Plot':
    fig = px.scatter(df, x=x_col, y=y_col, color=color)
    st.plotly_chart(fig)
elif plot_type == 'Histogram':
    fig2 = px.histogram(df, x=x_col)
    st.plotly_chart(fig2)

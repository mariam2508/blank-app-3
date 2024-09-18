import pandas as pd
import streamlit as st
st.header('file upload app')
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

import streamlit as st
import plotly.express as px

num_col = df.select_dtypes(include='number').columns.tolist()

tab1, tab2 = st.tabs(['Scatter Plot', 'Histogram'])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        x_col = st.selectbox('Choose x-axis', num_col, key='scatter_x')
    with col2:
        y_col = st.selectbox('Choose y-axis', num_col, key='scatter_y')
    with col3:
        color = st.selectbox('Choose color', num_col, key='scatter_color')

    # Create scatter plot
    fig = px.scatter(df, x=x_col, y=y_col, color=color)
    st.plotly_chart(fig)

with tab2:
    # Allow user to choose a column for the histogram x-axis
    hist_x_col = st.selectbox('Choose x-axis for histogram', num_col, key='hist_x')

    # Create histogram
    fig2 = px.histogram(df, x=hist_x_col)
    st.plotly_chart(fig2)

import streamlit as st
import pandas as pd
import numpy as np
import pickle

l_data = pd.read_csv('data/data3.csv')
l_data.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)

similarity = pickle.load(open('data/similarity.pkl','rb'))

title = st.title('Game Recommender system')

st.subheader('Choose game that you liked in past')

game = st.selectbox('',l_data['name'])

recommed = st.button('Recommend')
col1,col2 = st.columns(2)

if recommed:
    index = l_data[l_data['name'] == game].index[0]
    top_six = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:7]
    for i in range(len(top_six)):
        k = top_six[i][0]
        if i%2==0:
            with col1:
                st.image(l_data['header_image'][k])
                st.write(l_data['name'][k])
                st.write(l_data['genres'][k])
                #st.write(l_data['publisher'][k])
        else:
            with col2:
                st.image(l_data['header_image'][k])
                st.write(l_data['name'][k])
                st.write(l_data['genres'][k])
                #st.write(l_data['publisher'][k])


trending = st.subheader('Trending games')
col3,col4 = st.columns(2)
for i in range(4):
    if i % 2 == 0:
        with col3:
            st.image(l_data['header_image'][i])
            st.write(l_data['name'][i])
            st.write(l_data['genres'][i])
            # st.write(l_data['publisher'][k])
    else:
        with col4:
            st.image(l_data['header_image'][i])
            st.write(l_data['name'][i])
            st.write(l_data['genres'][i])
            # st.write(l_data['publisher'][k])
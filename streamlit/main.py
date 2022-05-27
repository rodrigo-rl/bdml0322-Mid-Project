import streamlit as st
import streamlit.components.v1 as components
from data.get_data import get_goles
 
st.title('Dashboard sobre el EURO-CUP 2020')
st.text('En este dashboar se va a ir enseñando datos sobre los equipos') 
st.text('participantes en la competición')

goles=get_goles()

st.text(type(goles))
st.text(goles)

for i in range(len(goles)):#:
    st.text(goles[i])
#st.json({'foo':'bar','fu':'ba'})
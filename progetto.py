#importiamo le librerie 
import polars as pl  
import streamlit as st
import altair as alt
import numpy as np

data =  pl.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv") #importo il file csv
print(data)

#i dati sono già tidy 
#per le analisi future trasformiamo il dataset in una matrice nunpy
md = data.to_numpy()

#vediamo le variabili presenti nel dataset

#costruiamo il titolo e l'introduzione
st.markdown("<h1 style='font-size: 45px;'>Remote Work & Mental Health</h1", unsafe_allow_html=True)
st.markdown("""As remote work becomes the new norm, it's essential to understand 
       its impact on employees' mental well-being. This dataset dives into
        how working remotely affects stress levels, work-life balance, and mental
        health conditions across various industries and regions.With 5,000 records
        collected from employees worldwide, this dataset provides valuable insights 
        into key areas like work location (remote, hybrid, onsite), stress levels,
        access to mental health resources, and job satisfaction. It’s designed to help researchers,
          HR professionals, and businesses assess the growing influence of remote work on productivity and well-being.""")

#prima introduzione sui dati

st.markdown("<h1 style='font-size: 40px;'>Introduction of our Sample</h1", unsafe_allow_html=True)

st.markdown("""As we can see from the graph below,  we are considering peaple of both genders, as well as non-binary peaple, nearly in equal number:""")
color_Gender = {
    "Female" : "pink", 
    "Male" : "blue",
    "Non-binary" : "yellow",
    "Prefer not to say" : "grey"

}
st.altair_chart(
    alt.Chart(data).mark_bar().encode(
        alt.X("count(Gender):Q"),
        alt.Y("Gender"),
        color = alt.Color("Gender:O", scale=alt.Scale(domain=list(color_Gender.keys()), range=list(color_Gender.values())))
    )
    .properties(height = 300, width = 600)
)




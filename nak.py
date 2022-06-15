import random 
import numpy as np
import streamlit as st


seas  = 13
ep = 9

with st.form(key="my_form"):
    seasons = st.number_input(label= "Antal Seasoner")
    eps = st.number_input(label="Antal Episoder")
    antal = st.number_input("Antal Foresalg")
    submit = st.form_submit_button("Submit")


if submit: 

    season = list(range(1, seas))
    eps = list(range(1,ep))

    pick = []
    for i in season:
        for ii in eps:
            pick.append(f"Season {i}, Episoide {ii}")


    for i in random.choices(pick, k=antal):
        st.write(i)

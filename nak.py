import random 
import numpy as np
import streamlit as st


seas  = 13
ep = 9

with st.form(key="my_form"):
    seasons = st.slider(label= "Antal Seasoner", min_value=1, max_value=12)
    eps = st.slider(label="Antal Episoder",min_value=1, max_value=10 )
    antal = st.text_input("Antal Foresalg")
    submit = st.form_submit_button("Submit")


if submit: 

    season = list(range(1, seas))
    eps = list(range(1,ep))

    pick = []
    for i in season:
        for ii in eps:
            pick.append(f"Season {int(i)}, Episoide {int(ii)}")


    for i in random.choices(pick, k=int(antal)):
        st.write(i)

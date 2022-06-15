import random 
import numpy as np
import streamlit as st



st.image("https://shop13443.sfstatic.io/upload_dir/shop/products/55/3155b.jpg")

with st.form(key="my_form"):
    seasons = st.slider(label= "Antal Seasoner", min_value=1, max_value=12)
    eps = st.slider(label="Antal Episoder",min_value=1, max_value=10 )
    antal = st.text_input("Antal Foresalg")
    submit = st.form_submit_button("Submit")


if submit: 

    season = list(range(1, seas))
    eps = list(range(1,ep))


    pick = [f"Season {int(x)}, Episode {int(y)}" for x in season for y in eps]


    for i in random.choices(pick, k=int(antal)):
        st.markdown(f'<div style="text-align: center;">{i}</div>', unsafe_allow_html=True)

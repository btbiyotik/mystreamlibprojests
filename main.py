import pandas as pd
import streamlit as st

df=pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
ulkeler=df["country"].unique()
ulke=st.sidebar.selectbox("Ülke seçiniz...",ulkeler)
df=df[df["country"]==ulke]
sehirler=df['city'].unique()
sehir=st.sidebar.selectbox('Şehir seçiniz...',sehirler)
df=df[df["city"]==sehir]

st.map(df)
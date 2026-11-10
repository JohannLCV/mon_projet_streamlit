import streamlit as st
import pandas as pd

st.title("Dashboard Analyse Taxis - Johann")

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"

df = pd.read_csv(URL)


arrondissements = sorted(df["pickup_borough"].dropna().unique())
choix_arrondissement = st.selectbox("Choisissez un arrondissement de prise en charge :", arrondissements)

paiement = sorted(df["payment"].dropna().unique())
choix_paiement = st.selectbox("Choisissez un mode de paiement :", paiement)

df_filtre = df[(df["pickup_borough"] == choix_arrondissement) & (df["payment"] == choix_paiement)]

st.metric("Nombre de courses", len(df_filtre))

st.dataframe(df_filtre.head())
# --- Imports ---
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- Titre de la page ---
st.title("Dashboard Vols ✈️")

# --- Chargement des données (mises en cache) ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    return pd.read_csv(url)

df = load_data()

# --- Filtres : plage d'années et mois ---
annees = st.slider("Plage d'années", min_value=1949, max_value=1960, value=(1949, 1960))
mois = ["Tous"] + df["month"].unique().tolist()   # liste des options du menu
choix_mois = st.selectbox("Choisissez un mois :", mois)

# --- Filtrage du tableau selon les choix ---
if choix_mois != "Tous":
    df_filtre = df[(df["year"] >= annees[0]) & (df["year"] <= annees[1]) & (df["month"] == choix_mois)]
else:
    df_filtre = df[(df["year"] >= annees[0]) & (df["year"] <= annees[1])]

# --- Tableau des données filtrées ---
st.dataframe(df_filtre)

# --- Indicateur : total de passagers sur la période ---
total_passagers = df_filtre["passengers"].sum()
st.metric("Nombre total de passagers", f"{total_passagers:,}".replace(",", " "))

# --- Graphique en lignes (Plotly) : évolution annuelle ---
evolution = df_filtre.groupby("year")["passengers"].sum().reset_index()

fig_ligne = px.line(
    evolution,
    x="year",
    y="passengers",
    labels={"year": "Année", "passengers": "Nombre de passagers"},
)
fig_ligne.update_xaxes(dtick=1, tickformat="d")   # une graduation par année, sans séparateur
fig_ligne.update_yaxes(tickformat=",")            # séparateur de milliers sur l'axe Y
fig_ligne.update_traces(
    hovertemplate="Année : %{x}<br>Nombre de passagers : %{y:,}<extra></extra>"
)                                                  # valeurs au survol avec séparateur
fig_ligne.update_layout(separators=", ")          # virgule décimale, espace pour les milliers
st.plotly_chart(fig_ligne)

# --- Heatmap (Seaborn) : passagers par année et par mois ---
if st.checkbox("Afficher la heatmap"):
    pivot = df_filtre.pivot(index="month", columns="year", values="passengers")
    pivot = pivot.reindex(mois[1:])   # mois dans l'ordre du calendrier
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(pivot, ax=ax, cbar_kws={"label": "Nombre de passagers"})
    ax.set_xlabel("Année")
    ax.set_ylabel("Mois")
    st.pyplot(fig)
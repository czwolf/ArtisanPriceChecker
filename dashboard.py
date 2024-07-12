import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


def get_data():
    file = r"C:\Users\hp\PycharmProjects\ArtisanPriceParser\data.csv"
    df = pd.read_csv(file, sep=";")
    transformed_df = pd.pivot_table(df, index='date', columns='name', values='price')
    transformed_df = transformed_df.reset_index()
    return transformed_df


data = get_data()

row1col1, row1col2, row1col3, = st.columns(3)

with row1col2:
    st.write("## Artisan KVH ceny")
    st.write(
        "[KVH hranoly NSi Smrk, délka 5000 - 40x100x5000](https://www.artisan.cz/kvh-hranoly-delka-5000-40x100x5000-m)")
    st.write(
        "[KVH hranoly NSi Smrk, délka 5000 - 40x120x5000](https://www.artisan.cz/kvh-hranoly-delka-5000-40x120x5000-u)")

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    h1, h2, h3 = st.columns(3)
    with h1:
        st.write("#### KVH hranoly 40x100x5000")

    row2col1, row2col2, row2col3, = st.columns(3)

    with row2col1:
        lower_price = data["kvh40x100x500"].min()
        st.metric("Nejnižší cena", round(lower_price, 1))

    with row2col2:
        max_price = data["kvh40x100x500"].max()
        st.metric("Nejvyšší cena", round(max_price, 1))

    with row2col3:
        mean_price = data["kvh40x100x500"].mean()
        st.metric("Průměrná cena", round(mean_price, 1))

with c2:
    h1, h2, h3 = st.columns(3)
    with h1:
        st.write("#### KVH hranoly 40x120x5000")
    row2col1, row2col2, row2col3, = st.columns(3)

    with row2col1:
        lower_price = data["kvh40x120x500"].min()
        st.metric("Nejnižší cena", round(lower_price, 1))

    with row2col2:
        max_price = data["kvh40x120x500"].max()
        st.metric("Nejvyšší cena", round(max_price, 1))

    with row2col3:
        mean_price = data["kvh40x120x500"].mean()
        st.metric("Průměrná cena", round(mean_price, 1))

fig = px.line(data, x='date', y=['kvh40x100x500', 'kvh40x120x500'])
st.plotly_chart(fig)

row3col1, row3col2, row3col3, = st.columns(3)

with row3col2:
    table_show = st.toggle(label="Tabulka dat")
    if table_show:
        st.dataframe(data)

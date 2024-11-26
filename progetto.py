import polars as pl
import streamlit as st
import altair as alt
#streamlit run nome file su terminale

data_url = pl.read_csv()




gapmider = pl.read_csv(data_url).filter(pl.col("year"))
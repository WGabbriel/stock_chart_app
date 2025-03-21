import streamlit
from data_science.grafic import plot_price

streamlit.title("Histórico de Cotações")
streamlit.write("Veja o histórico das cotações das empresas.")

ticker = streamlit.sidebar.text_input("Escolha o ticker:", value="GOOGL")
fig = plot_price(ticker)
streamlit.plotly_chart(fig)

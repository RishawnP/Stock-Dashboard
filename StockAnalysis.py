import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf # Yahoo finance
import plotly.express as px
from stocknews import StockNews # sn

st.title("Stock Dashboard")
ticker = st.sidebar.text_input("Ticker")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

data =yf.download(ticker,start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data["Adj Close"], title = ticker)
st.plotly_chart(fig)

pricing_data, news = st.tabs(["Pricing Data","Top 10 News"])

with pricing_data:
    st.header("Price Movements")
    updated_data = data
    updated_data["% Change"] = data["Adj Close"] / data["Adj Close"].shift(1) -1 # finds ADJ change by day
    updated_data.dropna(inplace = True) # nemoves #N/A from first value
    st.write(updated_data)
    annual_return = updated_data["% Change"].mean()*25200 #multiplied by days (252) and by (100) for percentage
    st.write("Annual Return Is ", annual_return, "%")
    stdev = np.std(updated_data["% Change"])*np.sqrt(252)
    st.write("standard Deveation Is ", stdev*100, "%") #convert to pertcentage
    st.write("Risk Adj. Return Is ", annual_return/(stdev*100))

with news:
    st.header(f"News for {ticker}")
    sn = StockNews(ticker, save_news = False)
    df_news = sn.read_rss() 
    for i in range(5): # i from 1 to 10
        st.subheader(f"News {i+1}")
        st.write(df_news["published"][i])
        st.write(df_news["title"][i])
        st.write(df_news["summary"][i])
        title_sentiment = df_news["sentiment_title"][i]
        st.write(f"Title Sentiment {title_sentiment}")
        news_sentiment = df_news["sentiment_summary"][i]
        st.write(f"News Sentiment {news_sentiment}")


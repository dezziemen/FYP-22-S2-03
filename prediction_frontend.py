import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from finance import CompanyStock
from training import LSTMPrediction


def candlestick(data):
    fig, ax = plt.subplots(figsize=(24, 4))
    color = ['green' if close_price > open_price else 'red' for close_price, open_price in zip(data['Close'], data['Open'])]
    plt.bar(x=data['Date'], height=np.abs(data['Open'] - data['Close']), bottom=np.min((data['Open'], data['Close']), axis=0), width=0.6, color=color)
    plt.bar(x=data['Date'], height=data['High'] - data['Low'], bottom=data['Low'], width=0.1, color=color)
    # plt.grid()
    return fig, ax


st.title('Stock prediction app')
symbol = st.text_input(label='Enter ticker symbol', placeholder='Ticker symbol')

company = CompanyStock(symbol)

if not company.company.info.get('symbol'):
    st.text('Company does not exist!')
else:
    st.header(company.get_info('shortName'))

    # Historical Data
    with st.container():
        st.subheader('Historical data')
        history = company.get_history().reset_index(level='Date')                       # Convert Date index to column
        history['Date'] = pd.to_datetime(history['Date']).dt.strftime('%d %b %Y')       # Convert Timestamp to Datetime

        # Setup graph
        fig, ax = candlestick(history)
        plt.xticks(rotation=90)                                                         # Rotate x-axis labels

        interval = int(len(history)/5)                                                  # Set intervals
        visible = ax.xaxis.get_ticklabels()[::interval]                                 # Hide some labels
        # Set invisible
        for label in ax.xaxis.get_ticklabels():
            if label not in visible:
                label.set_visible(False)
        # ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_formatter()))
        plt.savefig(f'{company.get_symbol()}_figure.png', dpi=300)
        st.pyplot(fig)

        st.write(history)

        if st.button('Predict stocks'):
            LSTMPrediction(company.get_close())

    # News
    with st.container():
        st.subheader('News')
        news = company.get_news()
        for article in news:
            title = article.get('title')
            link = article.get('link')
            link_str = f'[{title}]({link})'
            st.markdown(link_str)

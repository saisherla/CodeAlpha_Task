import streamlit as st
import yfinance as yf
import pandas as pd

# Session state for storing portfolio
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}

# Title
st.title("📈 Stock Portfolio Tracker")

# Sidebar for adding stocks
st.sidebar.header("➕ Add Stock")
ticker_input = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL)")
shares_input = st.sidebar.number_input("Number of Shares", min_value=1, step=1)
add_btn = st.sidebar.button("Add to Portfolio")

# Add stock to portfolio
if add_btn and ticker_input:
    ticker = ticker_input.upper()
    if ticker not in st.session_state.portfolio:
        st.session_state.portfolio[ticker] = shares_input
        st.success(f"Added {shares_input} shares of {ticker}")
    else:
        st.session_state.portfolio[ticker] += shares_input
        st.info(f"Updated {ticker} to {st.session_state.portfolio[ticker]} shares")

# Display portfolio
if st.session_state.portfolio:
    st.subheader("📊 Your Portfolio")

    data = []
    total_value = 0

    for ticker, shares in st.session_state.portfolio.items():
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get('regularMarketPrice', 0)
        previous_close = info.get('regularMarketPreviousClose', 0)
        change = price - previous_close
        value = shares * price
        total_value += value
        data.append({
            "Ticker": ticker,
            "Shares": shares,
            "Price": f"${price:.2f}",
            "Change": f"{change:+.2f}",
            "Value": f"${value:,.2f}"
        })

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    st.markdown(f"### 💰 Total Portfolio Value: ${total_value:,.2f}")

    # Remove stock
    st.subheader("❌ Remove Stock")
    remove_ticker = st.selectbox("Select stock to remove", list(st.session_state.portfolio.keys()))
    if st.button("Remove"):
        st.session_state.portfolio.pop(remove_ticker)
        st.success(f"Removed {remove_ticker} from portfolio")

else:
    st.info("Your portfolio is empty. Add some stocks to get started!")


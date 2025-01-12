# Stock-Dashboard

# Stock Dashboard

This is a simple Stock Dashboard application built using Streamlit, Yahoo Finance API, and Plotly for data visualization. The app allows users to input a stock ticker, specify a date range, and view the corresponding stock price movements and related news.

## Features
- **Stock Pricing Data Visualization**: Displays a line chart of the stock's adjusted closing prices over the specified date range.
- **Pricing Data Analysis**: Shows daily percentage changes, annual return, standard deviation, and risk-adjusted return.
- **Top 10 News Articles**: Fetches and displays the top 10 news articles for the specified stock ticker, including publication date, title, summary, and sentiment analysis.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.7 or higher
- Streamlit
- Pandas
- NumPy
- yfinance
- Plotly
- stocknews

You can install the required libraries using the following command:
```bash
pip install streamlit pandas numpy yfinance plotly stocknews
```

## Running the Application

1. Clone this repository or download the `StockAnalysis.py` file.
2. Open a terminal and navigate to the directory containing `StockAnalysis.py`.
3. Run the following command:
   ```bash
   streamlit run StockAnalysis.py
   ```
4. The application will open in your default web browser.

## Usage

1. Enter a valid stock ticker symbol in the sidebar (e.g., `AAPL` for Apple Inc.).
2. Select a start and end date for the data range.
3. View the stock price movements in the "Pricing Data" tab.
4. Check the top 10 related news articles in the "Top 10 News" tab, along with their sentiment analysis.

## Notes
- Ensure that the stock ticker symbol is valid and available on Yahoo Finance.
- The date range should be within the historical data available for the selected stock.

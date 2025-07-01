#IMPORTING LIBRARIES
import streamlit as st      #i am using StreamLit for UI,
import pandas as pd     #panda for Data handling, 
import matplotlib.pyplot as plt     # matplotlib for plotting graphs, 
import math     # math for advance calculations, 
import yfinance as yf       # and yfinance to import Stock Data
import plotly.express as px     #For Pichart and advance plotting
from bs4 import BeautifulSoup
import requests

#DATA OF TOP 90 COMPANY NAMES AND THEIR TICKERS
company_dict = {
    "Apple Inc.": "AAPL",
    "Microsoft Corporation": "MSFT",
    "Alphabet Inc. (Class A)": "GOOGL",
    "Alphabet Inc. (Class C)": "GOOG",
    "Amazon.com, Inc.": "AMZN",
    "Tesla, Inc.": "TSLA",
    "Meta Platforms, Inc.": "META",
    "NVIDIA Corporation": "NVDA",
    "Netflix, Inc.": "NFLX",
    "Intel Corporation": "INTC",
    "Advanced Micro Devices, Inc.": "AMD",
    "Adobe Inc.": "ADBE",
    "Cisco Systems, Inc.": "CSCO",
    "PayPal Holdings, Inc.": "PYPL",
    "PepsiCo, Inc.": "PEP",
    "The Coca-Cola Company": "KO",
    "NIKE, Inc.": "NKE",
    "Salesforce, Inc.": "CRM",
    "Oracle Corporation": "ORCL",
    "Broadcom Inc.": "AVGO",
    "Texas Instruments Incorporated": "TXN",
    "QUALCOMM Incorporated": "QCOM",
    "Costco Wholesale Corporation": "COST",
    "Walmart Inc.": "WMT",
    "McDonald's Corporation": "MCD",
    "The Boeing Company": "BA",
    "International Business Machines Corporation": "IBM",
    "Honeywell International Inc.": "HON",
    "General Electric Company": "GE",
    "Starbucks Corporation": "SBUX",
     "Johnson & Johnson": "JNJ",
    "Procter & Gamble Company": "PG",
    "UnitedHealth Group Incorporated": "UNH",
    "Visa Inc.": "V",
    "Mastercard Incorporated": "MA",
    "Pfizer Inc.": "PFE",
    "The Home Depot, Inc.": "HD",
    "Chevron Corporation": "CVX",
    "The Walt Disney Company": "DIS",
    "Comcast Corporation": "CMCSA",
    "Exxon Mobil Corporation": "XOM",
    "AbbVie Inc.": "ABBV",
    "Eli Lilly and Company": "LLY",
    "Merck & Co., Inc.": "MRK",
    "Bristol-Myers Squibb Company": "BMY",
    "Caterpillar Inc.": "CAT",
    "Lockheed Martin Corporation": "LMT",
    "3M Company": "MMM",
    "Raytheon Technologies Corporation": "RTX",
    "American Express Company": "AXP",
    "Goldman Sachs Group, Inc.": "GS",
    "Morgan Stanley": "MS",
    "Bank of America Corporation": "BAC",
    "Citigroup Inc.": "C",
    "JPMorgan Chase & Co.": "JPM",
    "Ford Motor Company": "F",
    "General Motors Company": "GM",
    "Delta Air Lines, Inc.": "DAL",
    "United Airlines Holdings, Inc.": "UAL",
    "Southwest Airlines Co.": "LUV",
    "Snowflake Inc.": "SNOW",
    "Zoom Video Communications, Inc.": "ZM",
    "Roku, Inc.": "ROKU",
    "Block, Inc.": "SQ",
    "Airbnb, Inc.": "ABNB",
    "Uber Technologies, Inc.": "UBER",
    "Lyft, Inc.": "LYFT",
    "DoorDash, Inc.": "DASH",
    "Palantir Technologies Inc.": "PLTR",
    "Robinhood Markets, Inc.": "HOOD",
    "Coinbase Global, Inc.": "COIN",
    "Moderna, Inc.": "MRNA",
    "BioNTech SE": "BNTX",
    "Regeneron Pharmaceuticals, Inc.": "REGN",
    "Illumina, Inc.": "ILMN",
    "Vertex Pharmaceuticals Incorporated": "VRTX",
    "Boston Scientific Corporation": "BSX",
    "Intuitive Surgical, Inc.": "ISRG",
    "Align Technology, Inc.": "ALGN",
    "DexCom, Inc.": "DXCM",
    "DocuSign, Inc.": "DOCU",
    "Twilio Inc.": "TWLO",
    "Zscaler, Inc.": "ZS",
    "Cloudflare, Inc.": "NET",
    "CrowdStrike Holdings, Inc.": "CRWD",
    "Datadog, Inc.": "DDOG",
    "Atlassian Corporation": "TEAM",
    "Shopify Inc.": "SHOP",
    "Sea Limited": "SE",
    "Pinterest, Inc.": "PINS"
}

#List contaning just company names for user selection
company_list = sorted(company_dict.keys())

#Main heading
st.markdown(
    "<h1 style='text-align: center;'>📊StockDog</h1>",
    unsafe_allow_html=True
)

#Title
st.title("Stock Market Graph Screener")

#user information section

st.write("### Your information")
col1, col2 = st.columns(2)
userName = col1.text_input(label = "What's Your Name?(optional)", value="You")
savings = col2.number_input("What's Your Current Savings in USD?(optional)", min_value=0, value=10000)
#selection box to input company name
company_name = st.selectbox(
    "Select or type a company name:",
    options=company_list,
    placeholder="Choose a company"
)
period = st.selectbox(options = ["1mo", "2mo","3mo", "6mo", "12mo"], placeholder="Enter the period", label = "Enter the period")

#checking the company name for error handling
if company_name:
    #coverting company Name to Ticker
    comp_symbol = company_dict.get(company_name.title())
    if comp_symbol:
        #to geather all the stock information as a DataFrame
        stock = yf.Ticker(comp_symbol)
        df = stock.history(period)
        #collecting start and end price from the "Close" column of DataFrame
        starting_price = df["Close"].iloc[0]
        ending_price = df["Close"].iloc[-1]
        #calculating the percentage of change in price
        change = ((ending_price/starting_price) - 1 ) * 100

        #Profit Display Section
        #CSS code to import and style with my own local Font(i am only using this font in Profit display)
        st.markdown("""
            <style>
            @font-face {
                font-family: 'PlayfairCustom';
                src: url('PlayfairDisplay-Bold.ttf') format('truetype');
            }

            .custom-text {
                font-family: 'PlayfairCustom';
                font-size: 36px;
                color: white;
                text-align: center;
                margin-bottom: 5px;
            }
            </style>
        """, unsafe_allow_html=True)
        #Display color as profit and loss
        if change > 0:
            st.markdown(f"<div class='custom-text'>📈 Profit: {change:.2f}%</div>", unsafe_allow_html=True)
        elif change < 0:
            st.markdown(f"<div class='custom-text' style='color: red;'>📉 Loss: {abs(change):.2f}%</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='custom-text' style='color: orange;'>No Change</div>", unsafe_allow_html=True)

        #GRAPH
        st.line_chart(df["Close"])

        #Other metrics
        current_price = stock.info.get("currentPrice")
        previous_close = stock.info.get("previousClose")
        market_cap = stock.info.get("marketCap",0)
        pe_ratio = stock.info.get("trailingPE")
        div_yield = stock.info.get("dividendYield")
        fifty_two_week_high = stock.info.get("fiftyTwoWeekHigh")
        
        if current_price and previous_close:
            change_percent = ((current_price - previous_close) / previous_close) * 100
            color = "green" if change_percent >= 0 else "red"
            st.markdown(f"<div class = custom-text>📈 Current Price: ${current_price:.2f}</div>",unsafe_allow_html=True)
            st.markdown(f"<span style='color:{color};text-align:centre;'><b>Daily Change:</b> {change_percent:.2f}%</span>", unsafe_allow_html=True)
        #making 2 columns to display metrics
        col1, col2 = st.columns(2)
        col1.metric("previous close:" ,f"${previous_close}")
        col1.metric("P/E ratio:" ,f"{pe_ratio:.2f}")
        col2.metric("Market cap:", f"${market_cap:,}" if market_cap else "N/A")
        col2.metric("Dividend Yield", f"{div_yield * 100:.2f}%" if div_yield else "N/A")

        #Last Sentence
        st.write("Estimate:")
        profit = ((savings * change)/100)
        st.write(f"If {userName} have invested {savings}USD {period} ago in {company_name}, {userName} would have extra {profit:.2f}USD sitting in the Bank Account")


        url = (f"https://techcrunch.com/?s={company_name}")
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        newsLink = {}

        st.title("Recent News:")
        for news in soup.find_all(class_="loop-card__title-link"):
            newsLink[news.get("data-destinationlink")] = news.get_text(strip=True)
        count = 0

        for link,news in newsLink.items():
            
            st.markdown(
                f"<a href='{link}' style='text-decoration: none; color: inherit;' target='_blank'>{news}</a>",
                unsafe_allow_html=True
            )
            st.write("")
            count+=1
            if count >=10:
                break
